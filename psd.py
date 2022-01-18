#!/bin/python
import sys
import argparse
import random
import urllib3
import os

static_link = "https://prnt.sc/"

letter_sequence = "abcdefghijklmnopqrstuvwxyz"
number_sequence = "1234567890"

letter_count = 2
number_count = 4

def random_download(download_ammount):
    # Keep downloading until app is canceled
    for ammount_to_download in range(download_ammount):
        imageId = ""

        # Create letters for Id
        for i in range(letter_count):
            imageId += random.choice(letter_sequence)

        # Create number for Id
        for i in range(number_count):
            imageId += random.choice(number_sequence)

        grab_image(imageId)


def grab_image(id):
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

    os.system("wget --output-document=./Downloads/image_" + id + ".png " + image_url)


parser = argparse.ArgumentParser(description="Download random screenshots from prnt.sc")
parser.add_argument("-a", "--ammount", help="Set the ammountof images you want to download", nargs="+")
args = parser.parse_args()

if args.ammount:
    random_download(int(args.ammount[0]))
else:
    print("Type -h or --help for instructions")
