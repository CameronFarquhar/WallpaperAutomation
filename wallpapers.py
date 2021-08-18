# import dependencies
import os
import requests
import wget
import ctypes
import time

from config import UNSPLASH_ACCESS_KEY




def get_wallpaper():
    # delete the previous wallpaper.jpg if it exists
    if os.path.exists('tmp/wallpaper.jpg'):
        os.remove('tmp/wallpaper.jpg')
    # create API query and define parameters
    url = 'https://api.unsplash.com/photos/random?client_id=' + UNSPLASH_ACCESS_KEY
    params = {
        "query": "HD Wallpapers",
        "orientation": "landscape"
    }
    # create request, define json format, grab image url, and save to folder
    response = requests.get(url, params=params).json()
    image_url = response['urls']['full']
    # download the image
    image = wget.download(image_url, 'tmp/wallpaper.jpg')
    print(image_url)
    return image


def change_wallpaper():
    get_wallpaper()
    # create path using cwd, current working directory, and use ctypes to update the deisgnated image as the wallpaper.
    # PATH = r'C:\Users\camer\OneDrive\Desktop\DataViz\My_Repo\Wallpaper_Automation\WallpaperAutomation\tmp\wallpaper (1).jpg'
    path = os.getcwd()+'\\tmp\\wallpaper.jpg'
    ctypes.windll.user32.SystemParametersInfoW(20,0, path,3)

def main():

	try:
		while True:
			change_wallpaper()
			time.sleep(10)

	except KeyboardInterrupt:
		print("\nThank you, come again!")
	except Exception as e:
		pass

    
if __name__ == "__main__":
    main()
