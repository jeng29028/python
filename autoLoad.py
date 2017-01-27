#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      home
#
# Created:     27/12/2014
# Copyright:   (c) home 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------


import os
import math
import string
import imageConvert as 圖轉換








def main():

    文件目錄 = "D:/類神經網路/貓/臉/"

    貓樣本=[]

    for dirPath, dirNames, fileNames in os.walk(文件目錄):
        for 檔名 in fileNames:
            路徑 = os.path.join(dirPath, 檔名)
            if('波斯' in 路徑):
                貓樣本.append([圖轉換.取灰階圖特徵值(路徑),[1,0,0,0,0]])
            elif('摺耳' in 路徑):
                貓樣本.append(["圖轉換.取灰階圖特徵值(路徑)",[0,1,0,0,0]])
            elif('無毛' in 路徑):
                貓樣本.append(["圖轉換.取灰階圖特徵值(路徑)",[0,0,1,0,0]])
            elif('達羅' in 路徑):
                貓樣本.append(["圖轉換.取灰階圖特徵值(路徑)",[0,0,0,1,0]])
            elif('狼貓' in 路徑):
                貓樣本.append(["圖轉換.取灰階圖特徵值(路徑)",[0,0,0,0,1]])


    print(貓樣本)



if __name__ == '__main__':
    main()
