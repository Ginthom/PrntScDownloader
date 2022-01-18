import random

from image_grabber import grab_image
from values import *

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