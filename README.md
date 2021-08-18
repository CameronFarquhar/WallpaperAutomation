<<<<<<< HEAD
Tired of the same old wallpapers? This program uses automation and the unsplash.com API to update your wallpaper every 10 seconds until you find one you like. 

description:

1) go to Unsplash.com and get a free API key. Don't forget to hide it in a config file if you want to upload your code to any file sharing site

2) import and/or download your dependencies.

3) create a folder names 'tmp' inside your working directory.

3.5) at this point you can copy and paste the code in to your code editor and it should run just fine if you are on Windows.

4) the get_wallpaper function deletes the previous wallpaper.jpg file if it exists, defines and calls the API path and request, then downloads the image into a tmp folder. If you do not want to download into a separate folder, just remove 'tmp' from the path.

5) the change_wallpaper function calls the get_wallpaper function, then changes the wallpaper using ctypes and the designated path to the file. 

6) using the try/except conditions, the main function calls the change_wallpaper function and uses the time package to run the program every 10 seconds. the except conditions allows the user to close out of the program, hence terminating the automation, when a desired wallpaper is found.

Hope you enjoy!
=======
[README.md](https://github.com/CameronFarquhar/WallpaperAutomation/files/7008756/README.md)
# WallpaperAutomation
>>>>>>> 0d45262faaf892ca414a9f73c9cc22ce7ec8f835
