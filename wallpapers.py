# import dependencies
import os
import requests
import wget
import ctypes
import random
import subprocess
from wallpaper import set_wallpaper, get_wallpaper
import time

from config import UNSPLASH_ACCESS_KEY


def get_wallpaper():
    # create API query and define parameters
    url = 'https://api.unsplash.com/photos/random?client_id=' + UNSPLASH_ACCESS_KEY
    params = {
        "query": "HD Wallpapers",
        "orientation": "Landscape"
    }
    # create request, difine json format, grab image url, and save to folder
    response = requests.get(url).json()
    image_url = response['urls']['full']

    image = wget.download(image_url, 'tmp/wallpaper.jpg')
    return image


def change_wallpaper():
    wallpaper = get_wallpaper()
    PATH = r'C:\Users\camer\OneDrive\Desktop\DataViz\My_Repo\Wallpaper_Automation\WallpaperAutomation\tmp\wallpaper.jpg'
    ctypes.windll.user32.SystemParametersInfoW(20,0, PATH,3)
    # os.remove("tmp/wallpaper.jpg")
    return wallpaper

def main():

	try:
		while True:
			change_wallpaper()
			time.sleep(10)

	except KeyboardInterrupt:
		print("\nHope you like this one! Quitting.")
	except Exception as e:
		pass


    
if __name__ == "__main__":
    main()
