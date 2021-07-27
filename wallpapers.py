# import dependencies
import os
import requests
import wget
from config import UNSPLASH_ACCESS_KEY

def main():
    # create API query and define parameters
    url = 'https://api.unsplash.com/photos/random?client_id=' + UNSPLASH_ACCESS_KEY
    params = {
        "query": "HD Wallpapers",
        "orientation": "Landscape"
    }
    # create request, difine json format, grab image url, and save to folder
    response = requests.get(url).json()
    image_url = response['urls']['full']
    wallpaper = wget.download(image_url, 'tmp/wallpaper.jpg')

    
if __name__ == "__main__":
    main()
