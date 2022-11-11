from urllib.request import urlopen
from bs4 import  BeautifulSoup
import pyfiglet

ascii_banner = pyfiglet.figlet_format(" Web Crawling")
print(ascii_banner)


html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')

for child in bs.find('table',{'id':'giftList'}).children:
	print(child)