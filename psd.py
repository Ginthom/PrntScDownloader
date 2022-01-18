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

def get_random_link():
    imageId = ""

    # Create letters for Id
    for i in range(letter_count):
        imageId += random.choice(letter_sequence)

    # Create number for Id
    for i in range(number_count):
        imageId += random.choice(number_sequence)

    return static_link + imageId
