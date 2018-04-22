import umllib2
from bs4 import BeautifulSoup

# dota2のwikiのヒーローページ
url = "https://dota2.gamepedia.com/Heroes";

html = urllib2.urlopen(url);

#mw-content-text > table:nth-child(2) > tbody > tr:nth-child(1)
#Bad_against\2e \2e \2e

#mw-content-text > span:nth-child(7) > b > a