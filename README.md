# Docker Ptt Crawler

### 安裝步驟
由於我的作業系統為 MacOS，故Docker主要參照 [Install Docker Desktop on Mac](https://docs.docker.com/docker-for-mac/install/)

* 從 Docker Hub 獲取我的 image
```
docker pull annie9512/docker-ptt-crawler
```
* Image 執行 Container
```
docker run -it annie9512/docker-ptt-crawler bash
```

### 使用步驟
* 執行 ptt_crawler.py
```
python ptt_crawler.py
```
* 輸入想抓取的看板
```
看板(All or Food or ....):
Food
```
* 輸入限定的日期區間
```
開始日期(2000/01/01): 2020/04/01
結束日期(2020/12/31): 2020/04/07
```
* 輸出結果並產生 csv
```
抓取看版: ['Food'], 頁數: 6951 - 7003
文章數: 148 (2020/04/01 00:00:00 - 2020/04/07 00:00:00 )
        authorId  authorName                             title board  ...                updateTime      commentId                  commentContent    commentTime
0    fish1234557          費雪          [食記] 台南 人氣爆棚雙生綠豆沙 葡吉水晶蛋糕  Food  ...  Mon Apr  6 17:50:43 2020          empty                           empty          empty
1           aner                     [食記] 台北醐同燒肉  沒感受到餐飲的不景氣阿？  Food  ...  Mon Apr  6 17:50:46 2020  04/02 01:55\n  : 我觀察了一個月, 結論就是主打年輕人中高消費店最沒影響,  04/02 01:55\n
2        smallta         冷笑生                  [食記] 台北 東區 果然匯蔬食  Food  ...  Mon Apr  6 17:50:47 2020          empty                           empty          empty
3        kamgx58         壽司羊     [食記] 高雄 KAKU 餐酒館 不貴的Prime肋眼牛排  Food  ...  Mon Apr  6 17:50:47 2020          empty                           empty          empty
4    JeremyKSKGA  Jeremy以食為天  [食記][台北市] 指有雞飯 Chicken Rice Only  Food  ...  Mon Apr  6 17:50:49 2020          empty                           empty          empty
..           ...         ...                               ...   ...  ...                       ...            ...                             ...            ...
143      NouTsan      Meteor                       [食記] 台北 東雛菊  Food  ...  Mon Apr  6 17:54:43 2020  04/03 16:13\n                     : 不錯的開場白 呵呵  04/03 16:13\n
144        larle    認命選擇保護自己                      [食記] 桃園。古弟私廚  Food  ...  Mon Apr  6 17:54:45 2020          empty                           empty          empty
145   love750219       討厭火星文                 [食記] 新北三重 超好吃素食麵線  Food  ...  Mon Apr  6 17:54:45 2020          empty                           empty          empty
146      Hanedas       南瓜塔塔麋      [食記]MoM's Touch師大店 韓國第二大速食品牌  Food  ...  Mon Apr  6 17:54:46 2020          empty                           empty          empty
147      b122771       四川缽缽雞       [食記] 新北.蘆洲 - ㄒㄧㄤˇ 精緻鍋物  涮涮鍋  Food  ...  Mon Apr  6 17:54:50 2020          empty                           empty          empty

[148 rows x 12 columns]
```
_為方便測試，有限制抓取頁數為50頁_