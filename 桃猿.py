import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json
from pitcherdata1 import pitcherdata1
from hitterdata import hitterdata
url = "http://www.cpbl.com.tw/web/team_player.php?&team=AJL011"
r = requests.get(url)
soup = BeautifulSoup(r.text,"html.parser")
players = soup.select(".gap_b20 tr td a") ## 所有打者
playerdata = {
    'player':[]
}
## 打者部分
playername ={
    'name':[]
}
for num in range(9,26):
    # 取得球員姓名
    name = players[num].text
    tmpdata1 = {
        name:[],
    }
    playername['name'].append(name)
    # 球員連結
    id = players[num].get('href').split('&')[1]
    url1 = 'http://www.cpbl.com.tw/players/follow.html?'+id+'&teamno=AJL011'
    r1 = requests.get(url1)
    soup1 = BeautifulSoup(r1.text,"html.parser")
    ## 球員表現
    data = soup1.select(".std_tb tr") # data為整個表格
    game = [0,0,0,0,0,0,0]
    for i in range(1,len(data)):
        month = int(data[i].select('td')[0].text.split('/')[0])
        # 月份 每位球員每個月出賽場次
        if month == 10:
            game[0] += 1
        elif month == 9:
            game[1] += 1
        elif month == 8:
            game[2] += 1
        elif month == 7:
            game[3] += 1
        elif month == 6:
            game[4] += 1
        elif month == 5:
            game[5] += 1
        else :
            game[6] += 1
        
    for i in range(1,len(game)+1):
        if game[i-1] == 0:
            monthdata = hitterdata(0,0,0,data)
        else :
            if i ==1 :
                monthdata = hitterdata(1,1,game[0],data)
            else :
                monthdata = hitterdata(1,sum(game[:i-1])+1,sum(game[:i]),data)
        tmpdata ={
            'month' :10-i+1,
            'data':{
                'PA':monthdata[0],
                'AB' :monthdata[1],
                'RBI' :monthdata[2],
                'R' :monthdata[3],
                'H' :monthdata[4],
                'B2' :monthdata[5],
                'B3' :monthdata[6],
                'HR' :monthdata[7],
                'TB' :monthdata[8],
                'SO' :monthdata[9],
                'SB' :monthdata[10],
                'CS' :monthdata[11],
                'AVG' :monthdata[12],
                'SAC' :monthdata[13],
                'SF' :monthdata[14],
                'BB' :monthdata[15],
                'IBB' :monthdata[16],
                'HBP' :monthdata[17],
                'GIDP' :monthdata[18],
                'TP':monthdata[19], 
                'LOB' :monthdata[20],
                'PO' :monthdata[21],
                'A' :monthdata[22],
                'DP' :monthdata[23],
                'TP' :monthdata[24],
                'E' :monthdata[25],
                'CS' :monthdata[26],
                'PB' :monthdata[27],
            }
        }
        tmpdata1[name].append(tmpdata)
    playerdata['player'].append(tmpdata1)
## 投手部分
for num in range(9):
    # 取得球員姓名
    name = players[num].text
    tmpdata1 = {
        name:[],
    }
    playername['name'].append(name)
    # 球員連結
    id = players[num].get('href').split('&')[1]
    url1 = 'http://www.cpbl.com.tw/players/follow.html?'+id+'&teamno=AJL011'
    url2 = 'http://www.cpbl.com.tw/players/apart.html?'+id+'&teamno=AJL011&year=2020&type=05'
    r1 = requests.get(url1)
    soup1 = BeautifulSoup(r1.text,"html.parser")
    r2 = requests.get(url2)
    soup2 = BeautifulSoup(r2.text,"html.parser")
    ## 球員表現
    data = soup1.select(".std_tb tr") # data為整個表格
    data2 = soup2.select(".std_tb tr")
    game = [0,0,0,0,0,0,0]
    IP = [0,0,0,0,0,0,0]
    for i in range(1,len(data)):
        month = int(data[i].select('td')[0].text.split('/')[0])
        # 月份 每位球員每個月出賽場次
        if month == 10:
            game[0] += 1
        elif month == 9:
            game[1] += 1
        elif month == 8:
            game[2] += 1
        elif month == 7:
            game[3] += 1
        elif month == 6:
            game[4] += 1
        elif month == 5:
            game[5] += 1
        else :
            game[6] += 1

    for i in range(1,len(data2)):
        Month1 = int(data2[i].select('td')[0].text.split('月')[0])
        if Month1 == 10:
            IP[0] = float(data2[i].select('td')[1].text)
        elif Month1 == 9:
            IP[1] = float(data2[i].select('td')[1].text)
        elif Month1 == 8:
            IP[2] = float(data2[i].select('td')[1].text)
        elif Month1 == 7:
            IP[3] = float(data2[i].select('td')[1].text)
        elif Month1 == 6:
            IP[4] = float(data2[i].select('td')[1].text)
        elif Month1 == 5:
            IP[5] = float(data2[i].select('td')[1].text)
        else :
            IP[6] = float(data2[i].select('td')[1].text)

    for i in range(1,len(game)+1):
        if game[i-1] == 0:
            monthdata = pitcherdata1(0,0,0,data)
        else :
            if i ==1 :
                monthdata = pitcherdata1(1,1,game[0],data)
            else :
                monthdata = pitcherdata1(1,sum(game[:i-1])+1,sum(game[:i]),data)
        tmpdata ={
            'month' :10-i+1,
            'data':{
                'IP' : IP[i-1],
                'BF' : monthdata[1],
                'NP' : monthdata[2],
                'H' : monthdata[3],
                'HR' : monthdata[4],
                'SO' : monthdata[5],
                'R' : monthdata[6],
                'ER' : monthdata[7],
                'BB' : monthdata[8],
                'IBB' : monthdata[9],
                'HBP' : monthdata[10],
                'AO' : monthdata[11],
                'GO' : monthdata[12],
                'CG' : monthdata[13],
                'SHO' : monthdata[14],
                'NBB' : monthdata[15],
                'BS' : monthdata[16],
                'NP2' : monthdata[17],
                'S' : monthdata[18],
                'SB': monthdata[19],
                'WP' : monthdata[20],
                'BK' : monthdata[21],
                'PO' : monthdata[22],
                'A' : monthdata[23],
                'DP' : monthdata[24],
                'TP' : monthdata[25],
                'E' : monthdata[26],
                'PK' : monthdata[27],
                'SV' : monthdata[28],
                'W' : monthdata[29],
                'L' : monthdata[30],
                'HLD' : monthdata[31],
            }
        }
        tmpdata1[name].append(tmpdata)
    playerdata['player'].append(tmpdata1)
jsonData = json.dumps(playerdata,ensure_ascii=False)
jsonData1 = json.dumps(playername,ensure_ascii=False)
# 儲存成檔案
f = open("桃猿2020.json","w",encoding="utf-8")
f1 = open("桃猿2020name.json","w",encoding="utf-8")
f.write(jsonData)
f1.write(jsonData1)
f.close()
f1.close()





