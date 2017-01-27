#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      jeng
#
# Created:     16/11/2014
# Copyright:   (c) jeng 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import re_bpnn_final as 倒傳遞函式
import imageConvert as 圖轉換



def main(檔案):


    貓臉網路 = 倒傳遞函式.神經網路(10, 8, 5,"測驗")


    貓測試 = [[圖轉換.取灰階圖特徵值(檔案)]]


    結果 = 貓臉網路.測驗(貓測試,1,"使用者")


    if(結果==1):
        return("波斯貓")

    elif(結果==2):
        return("摺耳貓")

    elif(結果==3):
        return("無毛貓")

    elif(結果==4):
        return("暹羅貓")

    elif(結果==5):
        return("狼貓")


if __name__ == '__main__':
    main()
