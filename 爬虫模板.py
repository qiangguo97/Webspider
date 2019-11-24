import requests
from lxml import etree

def get_url():
    url = ''
    headers = {}
    r = requests.get(url)
    r.encoding = r.apparent_encoding
    print(r.status_code)
    html = etree.HTML(r.text)
    bb = html.xpath('')
    bbs = "http:" + bb
    # print(bbs)
    t = requests.get(bbs)
    with open('tu.jpg','wb') as f:
        f.write(t.content)

if __name__ == "__main__":
    get_url()