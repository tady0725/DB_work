import datetime
import requests
from bs4 import BeautifulSoup
import sqlite3

# 開始測量
start = datetime.datetime.now()
c =1
recode=1
con = sqlite3.connect(
    "C:\\Users\\admin\\Desktop\\DB.Browser.for.SQLite-3.12.2-win64\\DB Browser for SQLite\\joke.sqlite")
al = con.execute("SELECT * FROM comment")
for k in range(1,7900):
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
            push = content.find_all('div', {'class': 'push'})


        except:
            continue
        for p in push:
            try:
                pushtag=p.find("span",{'class':'f1 hl push-tag'})
                pushid=p.find("span",{'class':'f3 hl push-userid'})
                pushcontent=p.find("span",{'class':'f3 push-content'})
                pushtime=p.find("span",{'class':'push-ipdatetime'})
                
                tag=pushtag.text.replace('"', '').replace("'", "")
                id_=pushid.text.replace('"', '').replace("'", "")
                content_=pushcontent.text.replace('"', '').replace("'", "")
                time=   pushtime.text.replace('"', '').replace("'", "")
                #a.append(pushcontent.text)
                recode+=1
                sql = "INSERT INTO comment (a_id,push_tag,push_userid,push_content,push_ipdatetime) VALUES"
                #print(sql)
                sql += "(\'"+str(c)+"\',\'"+str(tag)+"\',\'" + \
                    str(id_) + "\',\'"+str(content_)+"\',\'"+str(time)+"\'),"
                sql = sql[:-1]
            except :
                continue
            cc = con.execute(sql)
            
        c += 1
        con.commit()

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
