import numpy as np
#برای استفاده از ماتریکس

import random
#برای ساخت عدد تصادفی

#محاسبه زمان سپری شده برای پیدا کردن راه حل
#import time

#زمان شروع
#startTime = time.time()

chessBoard = np.zeros((8,8),int)
#ساخت صفحه سطرنج

for i in range(0,8):
    z = int(random.random()*10)%8
    chessBoard[z][i]=1

#محاسبه تعداد تهدید که چون هر وزیر دو بار برسی یمشود دو برابر تعداد زوج وزیرانی است که یکدیگر را تهدید میکنند
def calcute(board):
    NumberThreats = 0

    for x in range(0,8):
        for y in range (0,8):
            #پیدا کردن وزیر در هر ستون
            if(board[x][y]==1):
                y1 = y+1
                #جهت - محور ایکس
                while(y1<8):
                    if(board[x][y1]==1):
                        NumberThreats = NumberThreats+1
                    y1 = y1+1

                y1 = y-1
                #جهت + محور ایکس
                while(y1>-1):
                    if(board[x][y1]==1):
                        NumberThreats = NumberThreats+1
                    y1 = y1-1

                x1 = x+1
                y1 = y+1

                #محاسبه احتمالات تهدید اوریب در چهار چهت
                while(x1<8 and y1<8):
                    if(board[x1][y1]==1):
                        NumberThreats = NumberThreats+1
                    x1 =x1+1
                    y1 = y1+1


                x1 = x+1
                y1 = y-1
                while(x1<8 and y1>-1):
                    if(board[x1][y1]==1):
                        NumberThreats = NumberThreats+1
                    x1 =x1+1
                    y1 = y1-1


                x1 = x-1
                y1 = y+1
                while(x1>-1 and y1<8):
                    if(board[x1][y1]==1):
                        NumberThreats = NumberThreats+1
                    x1 =x1-1
                    y1 = y1+1


                x1 = x-1
                y1 = y-1
                while(x1>-1 and y1>-1):
                    if(board[x1][y1]==1):
                        NumberThreats = NumberThreats+1
                    
                    x1 =x1-1
                    y1 = y1-1
    #برگرداندن تعداد تهدید                
    return NumberThreats         



# برای اینکه در حلقه گرفتار نشویم  از روش 1 -حرکات کناره به حالت بعدی با امتیاز یکسان

counter = 0

while(1):
    counter = counter+1
    if(counter>100000):
        break
    if(calcute(chessBoard)==0):
        break
    
    #برای هر ستون برسی میکنیم
    for y in range(0,8):
        #یک کپی از صفحه اصلی میگیریم
        chessBoardcopy = np.copy(chessBoard)
        z=-1
        #خانه های که در صفحه اصلی است ر ستونی که قرار داریم وزیر موجود است را در ذخیره میکنیم
        for x in range(0,8):
            if (chessBoard[x][y]==1):
                chessBoardcopy[x][y]=0
                z=x
                break
        #به صورت یپش فرض انتخابی نداریم
        select = -1
        minimum = 1000    
        #برسی میکنیم که وزیر در کدام خانه که باشد تعداد تهدید کمتری داریم
        for x in range (0,8):
            #خانه ای که در صفحه اصلی پر است را در نظر نمیگیریم
            if (not(x==z)):
                chessBoardcopy[x][y]=1
                #هر انتخابی که تهدید کتری داشته باشد را ذخیره میکنیم
                if(calcute(chessBoardcopy)<minimum):
                    select = x
                    minimum = calcute(chessBoardcopy)
                chessBoardcopy[x][y]=0
        #در صورتی که انتخاب بهتری داشته باشیم بدون شرط انتخاب جدید را اعمال میکینم
        if(minimum<calcute(chessBoard)):
            chessBoard[z][y]=0
            chessBoard[select][y]=1
        #در صورتی که تعداد تهدید ها برار باشد به صورت تصادفی انتخاب میکنیم
        if(minimum==calcute(chessBoard)):
            if(random.random()<0.5):
                chessBoard[z][y]=0
                chessBoard[select][y]=1


print("tedad harkat = "+str(counter))
print(chessBoard)
print(calcute(chessBoard))