from bs4 import BeautifulSoup
import requests

def translate(input):
    """Takes string as input and returns the gizzoogled version of that string"""
    url = 'http://www.gizoogle.net/textilizer.php'
    payload = {'translatetext': input}
    r = requests.post(url,payload)
    soup = BeautifulSoup(r.content, "lxml")
    return soup.find(id='search_box').get_text().strip()
