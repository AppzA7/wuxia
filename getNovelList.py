import requests
import urllib.request
import shutil


base_url="https://www.wuxiaworld.com/novels/search?query="
trailer_url = "&count=10000"
    
if __name__ == "__main__":
    getList()
    download(base_url, "test")