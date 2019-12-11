import requests
from bs4 import BeautifulSoup
import lxml

url = "http://www.0376h.com/cbook_2056/1.html"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"
}
res = requests.get(url = url, headers = headers)

html = res.text
soup = BeautifulSoup(html, "lxml")
r = soup.find("div", id = "content")
texts = r.text.replace('\xa0'*4, '\n\n')
print(texts)
with open('xiaoshuo.txt', 'w') as f:
    f.write(texts)

