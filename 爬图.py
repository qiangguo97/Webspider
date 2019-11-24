import requests
from lxml import etree

def get_url(url):
    r = requests.get(url)
    print(r.status_code)
    r.encoding = r.apparent_encoding
    # print(r.text)
    html = etree.HTML(r.text)

    bc = html.xpath('//*[@id="lg"]/img[2]/@class')
    print(bc)
if __name__ == "__main__":
    url = 'http://www.baidu.com/'
    # headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"}
    get_url(url)
