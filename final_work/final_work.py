import datetime
import requests
from bs4 import BeautifulSoup
import sqlite3
def count_():
    f=open("countdata.csv","w")

    con = sqlite3.connect(
        "C:\\Users\\admin\\Desktop\\DB.Browser.for.SQLite-3.12.2-win64\\DB Browser for SQLite\\joke.sqlite")
    
    al=con.execute("SELECT * FROM article")
    
    
    allyear={"2001 Jan":0,
    "2001 Feb":0,
    "2001 Mar":0,
    "2001 Apr":0,
    "2001 May":0,
    "2001 Jun":0,
    "2001 Jul":0,
    "2001 Aug":0,
    "2001 Sep":0,
    "2001 Oct":0,
    "2001 Nov":0,
    "2001 Dec":0,
    "2002 Jan":0,
    "2002 Feb":0,
    "2002 Mar":0,
    "2002 Apr":0,
    "2002 May":0,
    "2002 Jun":0,
    "2002 Jul":0,
    "2002 Aug":0,
    "2002 Sep":0,
    "2002 Oct":0,
    "2002 Nov":0,
    "2002 Dec":0,
    "2003 Jan":0,
    "2003 Feb":0,
    "2003 Mar":0,
    "2003 Apr":0,
    "2003 May":0,
    "2003 Jun":0,
    "2003 Jul":0,
    "2003 Aug":0,
    "2003 Sep":0,
    "2003 Oct":0,
    "2003 Nov":0,
    "2003 Dec":0,
    "2004 Jan":0,
    "2004 Feb":0,
    "2004 Mar":0,
    "2004 Apr":0,
    "2004 May":0,
    "2004 Jun":0,
    "2004 Jul":0,
    "2004 Aug":0,
    "2004 Sep":0,
    "2004 Oct":0,
    "2004 Nov":0,
    "2004 Dec":0,
    "2005 Jan":0,
    "2005 Feb":0,
    "2005 Mar":0,
    "2005 Apr":0,
    "2005 May":0,
    "2005 Jun":0,
    "2005 Jul":0,
    "2005 Aug":0,
    "2005 Sep":0,
    "2005 Oct":0,
    "2005 Nov":0,
    "2005 Dec":0,
    "2006 Jan":0,
    "2006 Feb":0,
    "2006 Mar":0,
    "2006 Apr":0,
    "2006 May":0,
    "2006 Jun":0,
    "2006 Jul":0,
    "2006 Aug":0,
    "2006 Sep":0,
    "2006 Oct":0,
    "2006 Nov":0,
    "2006 Dec":0,
    "2007 Jan":0,
    "2007 Feb":0,
    "2007 Mar":0,
    "2007 Apr":0,
    "2007 May":0,
    "2007 Jun":0,
    "2007 Jul":0,
    "2007 Aug":0,
    "2007 Sep":0,
    "2007 Oct":0,
    "2007 Nov":0,
    "2007 Dec":0,
    "2008 Jan":0,
    "2008 Feb":0,
    "2008 Mar":0,
    "2008 Apr":0,
    "2008 May":0,
    "2008 Jun":0,
    "2008 Jul":0,
    "2008 Aug":0,
    "2008 Sep":0,
    "2008 Oct":0,
    "2008 Nov":0,
    "2008 Dec":0,
    "2009 Jan":0,
    "2009 Feb":0,
    "2009 Mar":0,
    "2009 Apr":0,
    "2009 May":0,
    "2009 Jun":0,
    "2009 Jul":0,
    "2009 Aug":0,
    "2009 Sep":0,
    "2009 Oct":0,
    "2009 Nov":0,
    "2009 Dec":0,
    "2010 Jan":0,
    "2010 Feb":0,
    "2010 Mar":0,
    "2010 Apr":0,
    "2010 May":0,
    "2010 Jun":0,
    "2010 Jul":0,
    "2010 Aug":0,
    "2010 Sep":0,
    "2010 Oct":0,
    "2010 Nov":0,
    "2010 Dec":0,
    "2011 Jan":0,
    "2011 Feb":0,
    "2011 Mar":0,
    "2011 Apr":0,
    "2011 May":0,
    "2011 Jun":0,
    "2011 Jul":0,
    "2011 Aug":0,
    "2011 Sep":0,
    "2011 Oct":0,
    "2011 Nov":0,
    "2011 Dec":0,
    "2012 Jan":0,
    "2012 Feb":0,
    "2012 Mar":0,
    "2012 Apr":0,
    "2012 May":0,
    "2012 Jun":0,
    "2012 Jul":0,
    "2012 Aug":0,
    "2012 Sep":0,
    "2012 Oct":0,
    "2012 Nov":0,
    "2012 Dec":0,
    "2013 Jan":0,
    "2013 Feb":0,
    "2013 Mar":0,
    "2013 Apr":0,
    "2013 May":0,
    "2013 Jun":0,
    "2013 Jul":0,
    "2013 Aug":0,
    "2013 Sep":0,
    "2013 Oct":0,
    "2013 Nov":0,
    "2013 Dec":0,
    "2014 Jan":0,
    "2014 Feb":0,
    "2014 Mar":0,
    "2014 Apr":0,
    "2014 May":0,
    "2014 Jun":0,
    "2014 Jul":0,
    "2014 Aug":0,
    "2014 Sep":0,
    "2014 Oct":0,
    "2014 Nov":0,
    "2014 Dec":0,
    "2015 Jan":0,
    "2015 Feb":0,
    "2015 Mar":0,
    "2015 Apr":0,
    "2015 May":0,
    "2015 Jun":0,
    "2015 Jul":0,
    "2015 Aug":0,
    "2015 Sep":0,
    "2015 Oct":0,
    "2015 Nov":0,
    "2015 Dec":0,
    "2016 Jan":0,
    "2016 Feb":0,
    "2016 Mar":0,
    "2016 Apr":0,
    "2016 May":0,
    "2016 Jun":0,
    "2016 Jul":0,
    "2016 Aug":0,
    "2016 Sep":0,
    "2016 Oct":0,
    "2016 Nov":0,
    "2016 Dec":0,
    "2017 Jan":0,
    "2017 Feb":0,
    "2017 Mar":0,
    "2017 Apr":0,
    "2017 May":0,
    "2017 Jun":0,
    "2017 Jul":0,
    "2017 Aug":0,
    "2017 Sep":0,
    "2017 Oct":0,
    "2017 Nov":0,
    "2017 Dec":0,
    "2018 Jan":0,
    "2018 Feb":0,
    "2018 Mar":0,
    "2018 Apr":0,
    "2018 May":0,
    "2018 Jun":0,
    "2018 Jul":0,
    "2018 Aug":0,
    "2018 Sep":0,
    "2018 Oct":0,
    "2018 Nov":0,
    "2018 Dec":0,
    "2019 Jan":0,
    "2019 Feb":0,
    "2019 Mar":0,
    "2019 Apr":0,
    "2019 May":0,
    "2019 Jun":0,
    "2019 Jul":0,
    "2019 Aug":0,
    "2019 Sep":0,
    "2019 Oct":0,
    "2019 Nov":0,
    "2019 Dec":0,
    "2020 Jan":0,
    "2020 Feb":0,
    "2020 Mar":0,
    "2020 Apr":0,
    "2020 May":0,
    "2020 Jun":0,
    "2020 Jul":0,
    "2020 Aug":0,
    "2020 Sep":0,
    "2020 Oct":0,
    "2020 Nov":0,
    "2020 Dec":0,
    "2021 Jan":0,
    "2021 Feb":0,
    "2021 Mar":0,
    "2021 Apr":0,
    "2021 May":0,
    "2021 Jun":0,
    "2021 Jul":0,
    "2021 Aug":0,
    "2021 Sep":0,
    "2021 Oct":0,
    "2021 Nov":0,
    "2021 Dec":0,
    
    }
    
    year=["2001","2002","2003",
    "2004",
    "2005",
    "2006",
    "2007",
    "2008",
    "2009",
    "2010",
    "2011",
    "2012",
    "2013",
    "2014",
    "2015",
    "2016",
    "2017",
    "2018",
    "2019",
    "2020",
    "2021"]
    
    month=["Jan","Feb","Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
    ]
    su={}
    
    for row in al:
        date=row[3]
        for k in year:
            y =str(k)
            for q in month:
                m=str(q)
                if  y in date and   m in date:
                    
                    name=str(y)+str(m)
                    if name not in su:
                        su[name]=1
                                            
                    else:
                        sums=su[name]
                        su[name]=sums+1
                        
    print(sum(su.values()))
    for key,values in su.items():
        f.write(str(key)+","+str(values)+"\n")
    f.close()
    
    con.commit()    
    
    con.close()

def ptt_writeSQl():


    # 開始測量
    start = datetime.datetime.now()
    # 7899
    c =0
    con = sqlite3.connect(
        "C:\\Users\\admin\\Desktop\\DB.Browser.for.SQLite-3.12.2-win64\\DB Browser for SQLite\\joke.sqlite")
    al = con.execute("SELECT * FROM article")
    for k in range(1, 7900):
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

            cc = con.execute(sql)

            con.commit()
            c += 1
    

            
    
    
    con.close()
    
    
    # 結束測量
    
    end = datetime.datetime.now()
    
    
    # 輸出結果
    print("執行時間：", end - start)