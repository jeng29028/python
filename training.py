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



def main():

    貓臉網路 = 倒傳遞函式.神經網路(10, 8, 5,"訓練")


    貓樣本=[]
    倒傳遞函式.自動取樣本("D:/類神經網路/貓/訓練/頭/",貓樣本)


    貓臉網路.訓練(貓樣本)

    狀態 = "訓練完畢"

    print(狀態)

    return 狀態


if __name__ == '__main__':
    main()
