#!/bin/python
import sys
import argparse
import random
import urllib3
import os

static_link = "https://prnt.sc/"

letter_sequence = "abcdefghijklmnopqrstuvwxyz"
number_sequence = "1234567890"

target_dir = "./Downloads"

letter_count = 2
number_count = 4

def random_download(download_amount, target_dir):
    # Keep downloading until app is canceled
    for amount_to_download in range(download_amount):
        imageId = ""

        # Create letters for Id
        for i in range(letter_count):
            imageId += random.choice(letter_sequence)

        # Create number for Id
        for i in range(number_count):
            imageId += random.choice(number_sequence)

        grab_image(imageId, target_dir)


def grab_image(id, target_dir):
    dynamic_link = static_link + id

    http = urllib3.PoolManager()
    result = http.request('GET', dynamic_link)
    test = str(result.data)

    index = test.find("https://image.prntscr.com/image/")
    print(index)
    image_name_end_index = test[index : index + 100].find(".png") + 4
    print(image_name_end_index)
    image_url = test[index : index + image_name_end_index]
    print(image_url)

    os.system(f"wget --output-document={target_dir}/image_{id}.png {image_url}")


parser = argparse.ArgumentParser(description="Download random screenshots from prnt.sc")
parser.add_argument("amount", help="Set the amountof images you want to download")
parser.add_argument("-d", "--dir", help="Change download directory")
args = parser.parse_args()

if args.dir:
    target_dir = args.dir

if args.amount:
    random_download(int(args.amount), target_dir)
else:
    print("Type -h or --help for instructions")
