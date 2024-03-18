#!/bin/python
import sys
import argparse
import random
import urllib3
import os
import string

static_link = "https://prnt.sc/"
target_dir = "./Downloads"

url_size = 6

def get_random_id():
    imageId = ""

    # Create letters for Id
    for i in range(url_size):
        imageId += random.choice(string.ascii_lowercase + string.digits)

    return imageId


def random_download(download_amount, target_dir):
    # Keep downloading until app is canceled
    counter = [download_amount, 0]
    for amount_to_download in range(download_amount):
        counter[1] += 1

        while not grab_image(get_random_id(), target_dir, counter):
            pass


def grab_image(id, target_dir, counter):
    dynamic_link = static_link + id

    http = urllib3.PoolManager()
    result = http.request('GET', dynamic_link)
    test = str(result.data)

    index = test.find("https://image.prntscr.com/image/")
    image_name_end_index = test[index : index + 100].find(".png") + 4
    image_url = test[index : index + image_name_end_index]
    try:
        http = urllib3.PoolManager()
        r = http.request('GET', image_url, preload_content=False)
        with open(f"{target_dir}/image_{id}.png", 'wb') as out:
            while True:
                data = r.read(64)
                if not data:
                    break
                out.write(data)
            r.release_conn()
        print(f"{counter[1]}/{counter[0]} {target_dir}/image_{id}.png")
        return True
    except:
        return False

parser = argparse.ArgumentParser(description="Download random screenshots from prnt.sc")
parser.add_argument("amount", help="Set the amount of images you want to download")
parser.add_argument("-d", "--dir", help="Change download directory")
args = parser.parse_args()

if args.dir:
    target_dir = args.dir

if args.amount:
    random_download(int(args.amount), target_dir)
else:
    print("Type -h or --help for instructions")
