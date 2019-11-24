import requests
from bs4 import BeautifulSoup
from lxml import etree


def get_url():
    url = 'http://699pic.com/video-sousuo-0-2-1-200-0-0.html?sem=1&sem_kid=126640&sem_type=2'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }  # 模拟浏览器
    r = requests.get(url, headers)
    r.encoding = 'UTF-8'
    # print(r.text)   #初学很必要，至少可以看到成功获取了所有网页源代码
    all_video = BeautifulSoup(r.text, 'lxml').find_all('video',class_='video-hover lazy')  # 找到所有属性为video-hover lazy的video节点
    # j = 0
    # l = []
    # for i in range(1, 100):
    #     l.append(i)  # 主要是用来命名，个人习惯用数字命名
    # for video in all_video:
    #     video_url = video['data-original']
    #     video_url = 'http:' + video_url
    #     print(video_url)  # 循环获取所有符合条件的img标签中的scr所指向的内容
    #     name = str(l[j])
    #     savefile(video_url, name)
    #     j += 1


# def savefile(video_url, name):
#     print("开始下载···")
#     video = requests.get(video_url)
#     file_name = name + '.mp4'
#     f = open('E://python//test//爬虫学习//视频素材' + '/' + file_name, 'ab')
#     print('开始保存视频')
#     f.write(video.content)
#     f.close()
#     html = etree.HTML(r.text)
#     bb = html.xpath('/html/body/div[2]/div[3]/ul/li[26]/a[1]/div/img/@data-original')[0]
#     bbs = "http:" +bb
#     print(bbs)
#     t = requests.get(bbs)
#     with open('shiping2.jpg','wb') as f:
#         f.write(t.content)
if __name__ == "__main__":
    get_url()
    # savefile()
