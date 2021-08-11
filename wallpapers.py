# import dependencies
import os
import requests
import wget
import ctypes
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
    get_wallpaper()
    PATH = r'C:\Users\camer\OneDrive\Desktop\DataViz\My_Repo\Wallpaper_Automation\WallpaperAutomation\tmp\wallpaper (1).jpg'
    ctypes.windll.user32.SystemParametersInfoW(20,0, PATH,3)



def main():

	try:
		while True:
            # os.remove("tmp/wallpaper (1).jpg")
			change_wallpaper()
			time.sleep(10)

	except KeyboardInterrupt:
		print("\nThank you, come again!")
	except Exception as e:
		pass


    
if __name__ == "__main__":
    main()
