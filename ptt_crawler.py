#%%
import requests
import pandas as pd
from bs4 import BeautifulSoup

def url_connect(url):
    # 設定header及18歲限制
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    return requests.get(url, cookies={'over18': '1'}, headers=headers)

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