import requests
from lxml import etree


# def get_url():
#     url = 'https://www.biquge18.com/book/131406/5087.html'
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362'
#     }  # 模拟浏览器
#     r = requests.get(url,headers)
#     r.encoding = r.apparent_encoding
#     # print(r.text)
#     html = etree.HTML(r.text)
#     ts = html.xpath("string(//body)")
#     print(ts)
#     # for t in ts:
    #     # 去掉空格换行之类的
    #     d = t.strip()
    #     print(d)
    #     save1File(d)

#
# def save1File(d):
#     print('''保存''')
#     with open('E:python//test//datas.txt', 'a', encoding='utf-8') as fp:
#         fp.write(d + '\n')


# get_url()
# save1File()

def get_url():
    url = 'https://www.baidu.com'
    r = requests.get(url)
    r.encoding = r.apparent_encoding
    html = etree.HTML(r.text)
    bd = html.xpath('//*[@id="u1"]/a[1]/text()')[0]
    hf = html.xpath('//*[@id="u1"]/a[1]/@href')[0]
    bf = html.xpath('//*[@id="u1"]/a[1]/@name')[0]
    bb = html.xpath('//*[@id="u1"]/a[6]/@href')[0]

    print(bc)
    # print(bb)
    # print(bd)
    # print(hf)
    # print(bf)
    # logo = html.xpath('//*[@id="lg"]/img[1]/@src')[0]
    # logos = 'http:' +logo
    # # print(logos)
    # t = requests.get(logos)
    # with open("baidu.jpg",'wb') as f:
    #     f.write(t.content)
if __name__ == "__main__":

    get_url()