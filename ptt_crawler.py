#%%
import requests
import pandas as pd
from bs4 import BeautifulSoup

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
    
    print("抓取看版: " + str(boards) + ", 頁數: " + str(20))

try:
    # 首頁
    url_index = "https://www.ptt.cc/bbs/index.html"
    res = url_connect(url_index)

except requests.exceptions.HTTPError as e:
    print ("Http Error:", e)
except requests.exceptions.ConnectionError as e:
    print ("Error Connecting:", e)
except requests.exceptions.Timeout as e:
    print ("Timeout Error:", e)
except requests.exceptions.RequestException as e:
    print ("OOps: Something Else", e)