import requests
import os
import urllib3

from values import static_link

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