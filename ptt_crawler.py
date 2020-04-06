#%%
import time
import datetime
import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime as dt

author_Id = []
author_Name = []
pub_Time = []
article_board = []
article_content = []
links = []
canonicalUrl = []
titles = []
comment_Id = []
comment_content = []
comment_time = []
boards = []
createdTime = []
updateTime = []

def url_connect(url):
    # 設定header及18歲限制
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    return requests.get(url, cookies={'over18': '1'}, headers=headers)

def get_Alllinks(boards=boards):
    latest_p = 0
    latest_link_p = ""
    for board in boards:
        url = "https://www.ptt.cc/bbs/" + board + "/index.html"
        res = url_connect(url)
        # html分解
        soup = BeautifulSoup(res.content, "html.parser")
        # 取得最新頁數
        pages_html = soup.findAll("a", {"class", "btn wide"})
        for page in pages_html:
            if "上頁" in page.text:
                latest_link_p = page.get("href")
                latest_p = int(latest_link_p[latest_link_p.index("index")+len("index"):latest_link_p.index(".")])
    
        # 取得所有連結 # 從最新的開始 # 限定頁數方便測試，刪除後則抓取全部
        for i in range(latest_p+1, latest_p-20, -1): 
            res = url_connect(url[:url.index(".html")] + str(i) + url[url.index(".html"):])
            # html分解
            items_html = soup.findAll("div", {"class", "r-ent"})
            for item in items_html:
                article = item.find('a')
                # 避免有文章刪除
                if article != []:
                    links.append("https://www.ptt.cc" + article.get('href'))
            # 休息 2 秒
            time.sleep(2)
    print("抓取看版: " + str(boards) + ", 頁數: " + str(20))

def get_articleInfo(All_links, datetime_start=dt.today()-datetime.timedelta(days=3), datetime_end=dt.today()):
    for link in All_links:
        res = url_connect(link)
        # html分解
        soup = BeautifulSoup(res.content, "html.parser")
        contents = soup.findAll("span", {"class", "article-meta-value"})
        # 取得文章時間
        article_time = dt.strptime(contents[3].text, "%a %b  %d %H:%M:%S %Y")
        # 判斷文章是否在時間範圍內
        if article_time > datetime_start and article_time < datetime_end:
            author_info = contents[0].text
            author_Id.append(author_info[:author_info.index(" (")])
            author_Name.append(author_info[author_info.index(" ("):author_info.index(")")])
            article_board.append(contents[1].text)
            titles.append(contents[2].text)
            pub_Time.append(contents[3].text)
            canonicalUrl.append(soup.findAll("link")[0].get("href"))
            article_content.append(soup.findAll("meta")[4].get("content"))
            createdTime.append(time.ctime())
            updateTime.append(time.ctime())
            # 抓取推文者資訊
            push_infos = soup.findAll("div", {"class", "push"})
            if push_infos != []:
                push_info = push_infos[0].findAll("span")
                comment_Id.append(push_info[1].text)
                comment_content.append(push_info[2].text)
                push_ipdate = push_info[3].text
                comment_time.append(push_ipdate[push_ipdate.index(" ")+1:])
            else:
                comment_Id.append("empty")
                comment_content.append("empty")
                comment_time.append("empty")
    print("文章數: " + str(len(titles)) + " (" + datetime_start.strftime("%Y/%m/%d %H:%M:%S") + " - " + datetime_end.strftime("%Y/%m/%d %H:%M:%S") + " )")

try:
    # 首頁
    url_index = "https://www.ptt.cc/bbs/index.html"
    res = url_connect(url_index)

    # html分解
    soup = BeautifulSoup(res.content, "html.parser")
    # 取得所有看版
    boards_html = soup.findAll("div", {"class", "board-name"})
    for b in boards_html:
        boards.append(b.text)

    in_board = input("看板(All or Food or ....): ")
    in_s_date = input("開始日期(2000/01/01): ")
    in_e_date = input("結束日期(2020/12/31): ")

    # 取得所有該版文章links
    if in_board == "All":
        get_Alllinks()
    else:
        get_Alllinks([in_board])

    # 抓取該鏈結的文章資訊 # 去重複連結
    get_articleInfo(list(set(links)), dt.strptime(in_s_date, "%Y/%m/%d"), dt.strptime(in_e_date, "%Y/%m/%d"))

    # 建立資料表
    ptt_data = pd.DataFrame({"authorId": author_Id,
                             "authorName": author_Name,
                              "title": titles,
                              "board": article_board,
                              "publishedTime": pub_Time,
                              "content": article_content,
                              "canonicalUrl": canonicalUrl,
                              "createdTime": createdTime,
                              "updateTime": updateTime,
                              "commentId": comment_time,
                              "commentContent": comment_content,
                              "commentTime": comment_time})

    ptt_data.to_csv('ptt_data.csv', index=False)
    print(ptt_data)

except requests.exceptions.HTTPError as e:
    print ("Http Error:", e)
except requests.exceptions.ConnectionError as e:
    print ("Error Connecting:", e)
except requests.exceptions.Timeout as e:
    print ("Timeout Error:", e)
except requests.exceptions.RequestException as e:
    print ("OOps: Something Else", e)