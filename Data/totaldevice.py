import requests
from bs4 import BeautifulSoup


#Used for to get total available device for to get characteristics

def totalDeviceChar():
    """
    return: int -> totalDevice
    """
    page = requests.get('https://fonoapi.freshpixl.com/')
    soup = BeautifulSoup(page.content, 'html.parser')

    return int(soup.find('input', {'id':'maxVal'}).get('value'))