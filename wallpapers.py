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

    wallpaper = wget.download(image_url, 'wallpaper.jpg')
    return wallpaper


def set_wallpaper():
    PATH = r'C:\Users\camer\OneDrive\Desktop\DataViz\My_Repo\Wallpaper_Automation\WallpaperAutomation\tmp\wallpaper.jpg'
    ctypes.windll.user32.SystemParametersInfoW(20,0, PATH,3)

def main():
  
# set your photo
    # set_wallpaper("tmp/wallpaper.jpg")


    # subprocess.Popen(cmd%wallpaper, shell=True)
	# subprocess.call(["killall Dock"], shell=True)


    # dir = r'tmp/wallpaper.jpg'
    # file=random.choice(os.listdir(dir))
    # wpp=(os.getcwd())
    # temp=('%s\%s'%(wpp,dir))
    # wpp=('%s\%s\%s'%(wpp,dir,file))
    # #typo(file)
    # #typo(wpp)
    # f=('%s\%s'%(dir,file))
    # #print('No files found')
    # ctypes.windll.user32.SystemParametersInfoW(20, 0,r"%s "%wpp , 0)
    
if __name__ == "__main__":
    main()
