import json
import numpy as np
from datamatrix import datamatrix,datamatrix1
## 資料輸入
with open('統一2020.json',encoding = 'utf8') as f :
    data = json.load(f)
with open('統一2020name.json',encoding = 'utf8') as f :
    name = json.load(f)
# 4月 : 6 ， 5月 : 5 ， 6月 : 4 ， 7月 : 3 ， 8月 : 2 ， 9月 : 1 ， 10月 : 0
month = int(input())
if month == 6:
    print('4月')
elif month == 5:
    print('5月')
elif month == 4:
    print('6月')
elif month == 3:
    print('7月')
elif month == 2:
    print('8月')
elif month == 1:
    print('9月')
else :
    print('10月')

matrixB = np.array([5,1,10,15,35,5,10])
for i in range(16):
    playername = name['name'][i]
    A = datamatrix(data,playername,i,month)
    matrixA = np.array(A)
    score = matrixA.dot(matrixB.T)
    #print(playername,A,score)
for i in range(16,28):
    playername = name['name'][i]
    A = datamatrix1(data,playername,i,month)
    matrixA = np.array(A)
    print(playername,A)

