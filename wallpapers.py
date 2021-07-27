import os
import requests

from config import UNSPLASH_ACCESS_KEY

def main():

    # access_key = os.environ.get('UNSPLASH_ACCESS_KEY')
    url = 'https://api.unsplash.com/photos/random?client_id=' + UNSPLASH_ACCESS_KEY
    response = requests.get(url)
    print(response.status_code)

    
if __name__ == "__main__":
    main()
