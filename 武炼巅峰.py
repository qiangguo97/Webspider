import re
import requests

url = 'https://www.xbiquge6.com/0_347/'
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"}
r = requests.get(url,headers=headers)
r.encoding = r.apparent_encoding
# print(r.status_code)
# print(r.text)
html = r.text
#获取小说名
title = re.findall(r'<h1>(.*?)</h1>',html)[0]
# print(title)
#获取章节信息
dl = re.findall(r'<div id="list">.*?</div>',html,re.S)[0]
#新建一个文件保存小说
fb = open('%s.txt'%title,'w',encoding='utf-8')
# print(dl)
chapter_info_list = re.findall(r'href="(.*?)">(.*?)<',dl,re.S)
# print(d1)
for chapter_info in chapter_info_list:
    chapter_title = chapter_info[1]
    chapter_url = chapter_info[0]
    # chapter_title,chapter_url = chapter_info
    # print(chapter_info)
    chapter_url = "https://www.xbiquge6.com%s" % chapter_url
    # print(chapter_url , chapter_title)
    #下载章节内容
    chapter_r = requests.get(chapter_url,headers=headers)
    chapter_r.encoding = chapter_r.apparent_encoding
    chapter_content = re.findall(r'<div id="content">(.*?)</div>',chapter_r.text,re.S)[0]
    #数据清洗
    chapter_content = chapter_content.replace(" ","")
    chapter_content = chapter_content.replace("&nbsp;","")
    chapter_content = chapter_content.replace("<br/>","")
    # print(chapter_content)
    fb.write(chapter_title)
    fb.write('\n')
    fb.write(chapter_content)
    fb.write('\n')
    print(chapter_title)

