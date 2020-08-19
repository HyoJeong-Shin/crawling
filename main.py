import requests
from bs4 import BeautifulSoup

f = open("naver_news.csv", "w", encoding='UTF-8')
f.write("언론사, 뉴스 제목\n") #분류

for n in range(1, 21, 10):
    raw = requests.get("https://search.naver.com/search.naver?&where=news&query=%EC%BD%94%EB%A1%9C%EB%82%98&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&cluster_rank=59&start="+str(n)+"&refresh_start=0")

    html = BeautifulSoup(raw.text, "html.parser")

    container = html.select("ul.type01 > li")

    for i in range(0, 10):

        try:
            title = container[i].select_one("a._sp_each_title").text
            media  = container[i].select_one("span._sp_each_source").text
            
            #print(media,title)
            title = title.replace(",", "")
            media = media[:-6]

            f.write(media + "," + title + "\n")
        except:
            continue

f.close()