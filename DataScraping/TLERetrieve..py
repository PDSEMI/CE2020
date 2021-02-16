import requests
from bs4 import BeautifulSoup
import urllib.request

url = "https://www.space-track.org/basicspacedata/query/class/gp/EPOCH/%3Enow-30/MEAN_MOTION/%3E11.25/ECCENTRICITY/%3C0.25/OBJECT_TYPE/payload/orderby/NORAD_CAT_ID,EPOCH/format/3le"
response = urllib.request.urlopen(url)
html = response.read()

soup = BeautifulSoup(html, "lxml")
table = soup.find("body")
print(table)