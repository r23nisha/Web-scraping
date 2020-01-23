import urllib.request
import urllib
from bs4 import BeautifulSoup
import os

def make_soup(url):
    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage,"html.parser")
    return soupdata

paylardatasaved = ""
soup = make_soup("https://www.basketball-reference.com/players/a/")
for record in soup.find_all('tr'):
    paylardata = ""
    for data in record.find_all('td'):
        paylardata = paylardata+","+data.text
    paylardatasaved = paylardatasaved + "\n" + paylardata[1:]

header = "player,From,To,pos,ht,wt,birth date,collage"+"\n"
file = open(os.path.expanduser("basketball.csv"),"wb")
file.write(bytes(header,encoding="ascii",errors="ignore"))
file.write(bytes(paylardatasaved,encoding="ascii",errors="ignore"))
