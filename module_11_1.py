from PIL import Image

image = Image.open('./image.png')
image = image.resize((200, 200))
image = image.convert('L')
image = image.rotate(90)
image.save('./image.png')


import requests
from bs4 import BeautifulSoup


def read_post(soup):
    return soup.findAll()


GENIUS_DEKMA_URL = 'https://genius.com/Dekma-nothing-has-changed-lyrics'
resp = requests.get(GENIUS_DEKMA_URL)
soup = BeautifulSoup(resp.text, "lxml")
desc = read_post(soup)
print(desc)
