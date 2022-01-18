import sys

from random_downloader import random_download
from iterating_downloader import iterating_download

try:
    download_ammount = int(sys.argv[1])
    download_order = sys.argv[2]
    first_id = sys.argv[3] 

except:
    print("There was an error with the command line arguments!\n"+
          "Please keep to the following format:\n"+
          "python psd.py <ammount to download> <i/r: download order> <the first it to download>")
    exit(-1)

if download_order == 'r':
    random_download(download_ammount)
elif download_order == 'i':
    iterating_download(download_ammount, first_id)

