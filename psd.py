import sys

from random_downloader import random_download
from iterating_downloader import iterating_download

try:
    download_ammount = int(sys.argv[1])

except:
    print("There was an error with the command line arguments!\n"+
          "Please keep to the following format:\n"+
          "python psd.py <ammount to download> <i/r: download order> <the first it to download>")
    exit(-1)

random_download(download_ammount)

