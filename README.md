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
開始日期(2000/01/01): 2020/03/20
結束日期(2020/12/31): 2020/04/07
```
* 輸出結果並產生csv
```
抓取看版: ['Food'], 頁數: 20
文章數: 7 (2020/03/20 00:00:00 - 2020/04/07 00:00:00 )
      authorId   authorName                                   title board  ...                updateTime      commentId commentContent    commentTime
0       AlphaD          DD            [食記] 台北大安 年三十 鐵板串燒居酒屋 幾乎刷菜單了  Food  ...  Mon Apr  6 14:59:38 2020          empty          empty          empty
1     shinyban         甩尼班  [食記] 台北中正—JellyJelly 慢工烘焙｜手作甜點起家的人氣咖啡廳  Food  ...  Mon Apr  6 14:59:39 2020          empty          empty          empty
2   suzukihiro       慢慢的等待                [食記] 台南保安路米糕 南部肉燥魚鬆混米糕讚！  Food  ...  Mon Apr  6 14:59:39 2020          empty          empty          empty
3  fish1234557          費雪               [食記] 嘉義 新生早點 大份量峰炸蛋餅 獨創口味  Food  ...  Mon Apr  6 14:59:40 2020          empty          empty          empty
4      Sipaloy          便當                             [請益] 想找山藥泥湯  Food  ...  Mon Apr  6 14:59:40 2020  04/06 20:13\n      : 我背脊有點發涼  04/06 20:13\n
5    oldfather   oldfather                 [食記] 台南 B.B特餐 民德分店 三色便當  Food  ...  Mon Apr  6 14:59:41 2020          empty          empty          empty
6   meiwen1201          娃娃         [食記] 台北北投 I'm here coffee (知行店)  Food  ...  Mon Apr  6 14:59:41 2020          empty          empty          empty

[7 rows x 12 columns]
```