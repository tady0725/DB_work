import datetime
import requests
from bs4 import BeautifulSoup
import sqlite3

# 開始測量
start = datetime.datetime.now()
allcontent = []
allauthor = []
alltitle = []
alldate = []
# 7899
c =118514
con = sqlite3.connect(
    "C:\\Users\\admin\\Desktop\\DB.Browser.for.SQLite-3.12.2-win64\\DB Browser for SQLite\\joke.sqlite")
al = con.execute("SELECT * FROM article")
for k in range(5963, 7900):
    print("第幾筆"+str(k))

    r = requests.get(
        "https://www.ptt.cc/bbs/joke/index"+str(k)+".html")

    r.encoding = "utf-8"

    soup = BeautifulSoup(r.text, "lxml")

    # print(table)
    try:    
        table = soup.find('div', {'class': 'r-list-container action-bar-margin bbs-screen'})
        rows = table.find_all('div', {'class': 'r-ent'})
    except:
        continue

    for i in rows:

        title = i.find('div', {'class': 'title'})
        t = title.find('a')
        try:
            s = (t['href'])
        except:
            continue
        # print(s)
        r1 = requests.get("https://www.ptt.cc"+s)
        soup1 = BeautifulSoup(r1.text, "lxml")
        content = soup1.find(id="main-content")
        # print(content.text)
        try:
            #author = content.find_all('div', {'class': 'article-metaline'})

            header = soup1.find_all('span', 'article-meta-value')

            main_container = soup1.find(id='main-container')
            # 把所有文字都抓出來
            all_text = main_container.text
            # 把整個內容切割透過 "-- " 切割成2個陣列
            pre_text = all_text.split('--')[0]

            # 把每段文字 根據 '\n' 切開
            texts = pre_text.split('\n')
            # 如果你爬多篇你會發現
            contents = texts[2:]
            # 內容
            fcontent = '\n'.join(contents)
            # 作者
            author = header[0].text.replace('"', '').replace("'", "")
            # 看版
            #board = header[1].text
            # 標題
            title = header[2].text.replace('"', '').replace("'", "")
            # 日期
            date = header[3].text.replace('"', '').replace("'", "")

        except:
            continue

        ss = fcontent.replace('"', '').replace("'", "")
        sql = "INSERT INTO article (a_id,author,title,time,content) VALUES"
        sql += "(\'"+str(c)+"\',\'"+str(author)+"\',\'" + \
            str(title) + "\',\'"+str(date)+"\',\'"+str(ss)+"\'),"
        sql = sql[:-1]
        # print(sql)

        cc = con.execute(sql)
        # print(cc.rowcount)
        con.commit()
        c += 1

        # print('作者：'+author)
        # print('看板：'+board)
        # print('標題：'+title)
        # print('日期：'+date)

        # allcontent.append(fcontent)
        #allauthor.append( author)
        # alltitle.append(title)
        # alldate.append(date)
        


con.close()


# 結束測量

end = datetime.datetime.now()


# 輸出結果
print("執行時間：", end - start)

# print('內容：'+fcontent)
'''
    for k in author:

        try:
            s = (k.text)
            # print(s)
        except:
            continue
'''
