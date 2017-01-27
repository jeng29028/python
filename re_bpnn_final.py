"""
演算法程式原作者:
Neil Schemenauer <nas@arctrix.com>
"""
import os
import math
import random
import string
import time, itertools
import imageConvert as 圖轉換


random.seed() #不固定每次亂數取法

#取a到b之間的亂數(不包含b)
def 取亂數(a,b):
    return (b-a)*random.random() + a


def 建矩陣(I,J,fill=0.0):
        m = []
        for i in range(I):
            m.append([fill]*J)
        return m

def sigmoid(x):
    return math.tanh(x)

def dsigmoid(y):
    return 1.0 - y**2

#..........................................................
class 神經網路:
    def __init__(self, 輸入節點數, 隱藏層節點數, 輸出節點數,模式="訓練",部位="頭"):
        # 三層之節點數目
        self.輸入節點數 = 輸入節點數 #+ 1 # +1 for bias node
        self.隱藏層節點數 = 隱藏層節點數
        self.輸出節點數 = 輸出節點數

        # 節點激發的結果
        self.輸入點激發結果 = [1.0]*self.輸入節點數
        self.隱藏點激發結果 = [1.0]*self.隱藏層節點數
        self.輸出點激發結果 = [1.0]*self.輸出節點數

        # 設置權重
        self.輸入節點權重 = 建矩陣(self.輸入節點數, self.隱藏層節點數)
        self.輸出節點權重 = 建矩陣(self.隱藏層節點數, self.輸出節點數)

        if(模式=="訓練"):
            # 亂數初始權重
            for i in range(self.輸入節點數):
                for j in range(self.隱藏層節點數):
                    #self.輸入節點權重[i][j] = random.random()
                    self.輸入節點權重[i][j] = 取亂數(-10, 10)

            for j in range(self.隱藏層節點數):
                for k in range(self.輸出節點數):
                    #self.輸出節點權重[j][k] = random.random()
                    self.輸出節點權重[j][k] = 取亂數(-10, 10)


        if(模式=="測驗"):
            if(部位=="頭"):
                輸入層權重來源 = open('輸入權重(頭).txt')#,encoding='UTF-8')
                輸出層權重來源 = open('輸出權重(頭).txt')#,encoding='UTF-8')
            elif(部位=="左耳"):
                輸入層權重來源 = open('輸入權重(左耳).txt')#,encoding='UTF-8')
                輸出層權重來源 = open('輸出權重(左耳).txt')#,encoding='UTF-8')
            elif(部位=="右耳"):
                輸入層權重來源 = open('輸入權重(右耳).txt')#,encoding='UTF-8')
                輸出層權重來源 = open('輸出權重(右耳).txt')#,encoding='UTF-8')
            elif(部位=="臉"):
                輸入層權重來源 = open('輸入權重(臉).txt')#,encoding='UTF-8')
                輸出層權重來源 = open('輸出權重(臉).txt')#,encoding='UTF-8')


            輸入層權重 = 輸入層權重來源.readlines()			#依行讀入至List
            輸入層權重來源.close()
            輪到順序 = 0
            for i in range(self.輸入節點數):
                for j in range(self.隱藏層節點數):
                    輸入權重 = float(輸入層權重[輪到順序])
                    self.輸入節點權重[i][j] = 輸入權重
                    輪到順序+=1


            輸出層權重 = 輸出層權重來源.readlines()			#依行讀入至List
            輸出層權重來源.close()
            輪到順序 = 0
            for j in range(self.隱藏層節點數):
                for k in range(self.輸出節點數):
                    輸出權重 = float(輸出層權重[輪到順序])
                    self.輸出節點權重[j][k] = 輸出權重
                    輪到順序+=1


        # last change in weights for momentum
        self.ci = 建矩陣(self.輸入節點數, self.隱藏層節點數)
        self.co = 建矩陣(self.隱藏層節點數, self.輸出節點數)

#............
    def 更新(self, 輸入值):

        if len(輸入值) != self.輸入節點數:
            raise ValueError('錯誤的輸入')

        # 激發輸入層
        for i in range(self.輸入節點數):
            #self.輸入點激發結果[i] = sigmoid(輸入值[i])
            self.輸入點激發結果[i] = 輸入值[i]


        # 激發隱藏層
        for j in range(self.隱藏層節點數):
            加總結果 = 0.0
            for i in range(self.輸入節點數):
                加總結果 = 加總結果 + self.輸入點激發結果[i] * self.輸入節點權重[i][j]
            self.隱藏點激發結果[j] = sigmoid(加總結果)

        # 激發輸出層
        for k in range(self.輸出節點數):
            加總結果 = 0.0
            for j in range(self.隱藏層節點數):
                加總結果 = 加總結果 + self.隱藏點激發結果[j] * self.輸出節點權重[j][k]
            self.輸出點激發結果[k] = sigmoid(加總結果)


        return self.輸出點激發結果[:]
#.....................

    def 倒傳遞(self, 目標值, 學習率, M,部位):

        if(部位=="頭"):
            輸入權重檔 = open("輸入權重(頭).txt","w",encoding = 'UTF-8')
            輸出權重檔 = open("輸出權重(頭).txt","w",encoding = 'UTF-8')
        elif(部位=="左耳"):
            輸入權重檔 = open("輸入權重(左耳).txt","w",encoding = 'UTF-8')
            輸出權重檔 = open("輸出權重(左耳).txt","w",encoding = 'UTF-8')
        elif(部位=="右耳"):
            輸入權重檔 = open("輸入權重(右耳).txt","w",encoding = 'UTF-8')
            輸出權重檔 = open("輸出權重(右耳).txt","w",encoding = 'UTF-8')
        elif(部位=="臉"):
            輸入權重檔 = open("輸入權重(臉).txt","w",encoding = 'UTF-8')
            輸出權重檔 = open("輸出權重(臉).txt","w",encoding = 'UTF-8')


        if len(目標值) != self.輸出節點數:
            raise ValueError('錯誤的目標值')

        # 計算輸出層誤差
        輸出層變化 = [0.0] * self.輸出節點數
        for k in range(self.輸出節點數):
            誤差 = 目標值[k]-self.輸出點激發結果[k]
            輸出層變化[k] = dsigmoid(self.輸出點激發結果[k]) * 誤差

        # 計算隱藏層誤差
        隱藏層變化 = [0.0] * self.隱藏層節點數
        for j in range(self.隱藏層節點數):
            誤差 = 0.0
            for k in range(self.輸出節點數):
                誤差 = 誤差 + 輸出層變化[k]*self.輸出節點權重[j][k]
            隱藏層變化[j] = dsigmoid(self.隱藏點激發結果[j]) * 誤差

        # 更新輸出權重
        for j in range(self.隱藏層節點數):
            for k in range(self.輸出節點數):
                變量 = 輸出層變化[k]*self.隱藏點激發結果[j]
                self.輸出節點權重[j][k] = self.輸出節點權重[j][k] + 學習率*變量 + M*self.co[j][k]
        #把輸出權重存成一個檔
                輸出權重 = str(self.輸出節點權重[j][k])
                輸出權重檔.write(輸出權重 + "\n")
                self.co[j][k] = 變量

        # 更新輸入權重
        for i in range(self.輸入節點數):
            for j in range(self.隱藏層節點數):
                變量 = 隱藏層變化[j]*self.輸入點激發結果[i]
                self.輸入節點權重[i][j] = self.輸入節點權重[i][j] + 學習率*變量 + M*self.ci[i][j]
        #把輸入權重存成一個檔
                輸入權重 = str(self.輸入節點權重[i][j])
                輸入權重檔.write(輸入權重 + "\n")
                self.ci[i][j] = 變量


        輸入權重檔.close()
        輸出權重檔.close()


        # 計算誤差
        誤差 = 0.0
        for k in range(len(目標值)):
            誤差 = 誤差 + 0.5*(目標值[k]-self.輸出點激發結果[k])**2
        return 誤差


    def 測驗(self, patterns, 方法=1,模式="除蟲",正確答案=dict(), 檔名陣列=[]):

        測驗總數 = 0
        正確數 = 0

        if(方法==1):
            if(模式=="使用者"):
                for p in patterns:
                    測驗結果 = self.更新(p[0])
                    print(p[0], '->', 測驗結果)

                    最可能的類型 = 0
                    最大值 = 0
                    for i in range(len(測驗結果)):
                        if (測驗結果[i]>最大值):
                            最大值 = 測驗結果[i]
                            最可能的類型 = i + 1
                return(最可能的類型)

            else:
                for p in patterns:
                    測驗結果 = self.更新(p[0])
                    print(p[0], '->', 測驗結果)
                    測驗總數 +=1

                    最可能的類型 = 0
                    最大值 = 0
                    for i in range(len(測驗結果)):
                        if (測驗結果[i]>最大值):
                            最大值 = 測驗結果[i]
                            最可能的類型 = i + 1
                    if(最可能的類型 == 正確答案[檔名陣列[測驗總數-1]]):
                        正確數 +=1

                正確率 = float(正確數/測驗總數)
                print("方法1正確率",正確率*100,"%")


        elif(方法==2):
            for p in patterns:
                測驗結果 = self.更新(p[0])
                print(p[0], '->', 測驗結果)

                最可能的類型 = 0
                最大值 = 0
                for i in range(len(測驗結果)):
                    if (測驗結果[i]>最大值):
                        最大值 = 測驗結果[i]
                        最可能的類型 = i + 1
            return(最可能的類型,最大值)


        #print("我推測是",最可能的類型)
        #return(最可能的類型)


    #-----------------------------11/15重大發現，訓練次數一多(如破千次)會造成網路訓練時會有遺忘先學的傾向
    #-----------------------------最大問題: 訓練到何時該停止?
    def 訓練(self, patterns,部位,y=0, 訓練次數=2000, 學習率=0.5, M=0.1):
        # M: momentum factor
        舊誤差 = 0
        次數 = 0
        for i in range(訓練次數):
            誤差 = 0.0
            for p in patterns:
                輸入值 = p[0]
                目標值 = p[1]
                self.更新(輸入值)
                if(i>0):
                    舊誤差 = 誤差
                誤差 = 誤差 + self.倒傳遞(目標值, 學習率, M, 部位)
                新誤差 = 誤差
            """
            if(新誤差>舊誤差):
                次數+=1
            if(次數>1):
                break
            """
            if(y==0):
                if i % 100 == 0:            #每訓練100次輸出誤差一次
                    print('誤差 %-.5f' % 誤差)



def 自動取樣本(目錄,陣列):

    文件目錄 = 目錄
    樣本=[]
    樣本 = 陣列

    for dirPath, dirNames, fileNames in os.walk(文件目錄):
        for 檔名 in fileNames:
            路徑 = os.path.join(dirPath, 檔名)
            if('波斯' in 路徑):
                樣本.append([圖轉換.取灰階圖特徵值(路徑),[1,0,0,0,0]])
            elif('摺耳' in 路徑):
                樣本.append([圖轉換.取灰階圖特徵值(路徑),[0,1,0,0,0]])
            elif('無毛' in 路徑):
                樣本.append([圖轉換.取灰階圖特徵值(路徑),[0,0,1,0,0]])
            elif('暹羅' in 路徑):
                樣本.append([圖轉換.取灰階圖特徵值(路徑),[0,0,0,1,0]])
            elif('狼貓' in 路徑):
                樣本.append([圖轉換.取灰階圖特徵值(路徑),[0,0,0,0,1]])


def 自動取測試(目錄,陣列,字典,檔名陣列):

    文件目錄 = 目錄
    樣本=[]
    樣本 = 陣列
    正確答案字典 = dict()
    正確答案字典 = 字典

    for dirPath, dirNames, fileNames in os.walk(文件目錄):
        for 檔名 in fileNames:
            路徑 = os.path.join(dirPath, 檔名)
            檔名陣列.append(路徑)
            樣本.append([圖轉換.取灰階圖特徵值(路徑)])
            if('波斯' in 路徑):
                正確答案字典[路徑] = 1
            elif('摺耳' in 路徑):
                正確答案字典[路徑] = 2
            elif('無毛' in 路徑):
                正確答案字典[路徑] = 3
            elif('暹羅' in 路徑):
                正確答案字典[路徑] = 4
            elif('狼貓' in 路徑):
                正確答案字典[路徑] = 5

#..................................................................

def demo(方法=1,模式="訓練"):

    #訓練樣本一多會造成辨識結果有可能造成錯亂
    #------------------------------11/15發現這裡的"結果會依存於最後一個樣本" 目前最大問題
    #--------------(重大突破)----------------12/18確認輸入值為0~1之間時有最好的辨識效果，就不會被多筆訓練資料影響(而且誤差確實逐漸縮小)

    起始時間 = time.time()

    if(方法==1):
        #自動取貓樣本
        貓樣本=[]
        自動取樣本("D:/類神經網路/貓/訓練/頭/",貓樣本)
        #--------------------------------------------------------
        if(模式=="訓練"):
            n = 神經網路(10, 8, 5)
            n.訓練(貓樣本,"頭")
        elif(模式=="測驗"):
            n = 神經網路(10, 8, 5,模式,"頭")

        正確答案 = dict()
        貓測試 =[]
        檔名陣列 =[]
        自動取測試("D:/類神經網路/貓/測試/頭/",貓測試,正確答案,檔名陣列)

        n.測驗(貓測試,1,"除蟲",正確答案,檔名陣列)
    #----------------------------------------------到此為方法1



    elif(方法==2):

        右耳樣本=[]
        自動取樣本("D:/類神經網路/貓/訓練/右耳/",右耳樣本)

        左耳樣本=[]
        自動取樣本("D:/類神經網路/貓/訓練/左耳/",左耳樣本)

        臉樣本=[]
        自動取樣本("D:/類神經網路/貓/訓練/臉/",臉樣本)

        if(模式=="訓練"):
            右耳 = 神經網路(10, 8, 5)
            左耳 = 神經網路(10, 8, 5)
            臉 = 神經網路(10, 8, 5)

            右耳.訓練(右耳樣本,"右耳")
            print("以上右耳")
            左耳.訓練(左耳樣本,"左耳")
            print("以上左耳")
            臉.訓練(臉樣本,"臉")
            print("以上臉")

        elif(模式=="測驗"):
            右耳 = 神經網路(10, 8, 5,模式,"右耳")
            左耳 = 神經網路(10, 8, 5,模式,"左耳")
            臉 = 神經網路(10, 8, 5,模式,"臉")


        測驗總數 = 0
        正確數 = 0
        種類個數 = dict()
        正確的種類 = 0
        for dirPath, dirNames, fileNames in os.walk("D:/類神經網路/貓/測試/右耳/"):
            for 檔名 in fileNames:
                測驗總數 +=1

                for x in range(5):
                    種類個數[x+1] =0

                if('波斯' in 檔名):
                    正確的種類 = 1
                elif('摺耳' in 檔名):
                    正確的種類 = 2
                elif('無毛' in 檔名):
                    正確的種類 = 3
                elif('暹羅' in 檔名):
                    正確的種類 = 4
                elif('狼貓' in 檔名):
                    正確的種類 = 5

                路徑 = os.path.join("D:/類神經網路/貓/測試/右耳/", 檔名)
                右耳測試 = [[圖轉換.取灰階圖特徵值(路徑)]]

                路徑 = os.path.join("D:/類神經網路/貓/測試/左耳/", 檔名)
                左耳測試 = [[圖轉換.取灰階圖特徵值(路徑)]]

                路徑 = os.path.join("D:/類神經網路/貓/測試/臉/", 檔名)
                臉測試 = [[圖轉換.取灰階圖特徵值(路徑)]]


                三部分結果 = dict()

                右耳結果,右耳值 = 右耳.測驗(右耳測試,方法=2)
                種類個數[右耳結果]+=1
                三部分結果["右耳"]= 右耳結果

                左耳結果,左耳值 = 左耳.測驗(左耳測試,方法=2)
                種類個數[左耳結果]+=1
                三部分結果["左耳"]= 左耳結果

                臉結果,臉值 = 臉.測驗(臉測試,方法=2)
                種類個數[臉結果]+=1
                三部分結果["臉"]= 臉結果

                最可能的種類= 0
                for z in range(5):
                    if(種類個數[z+1] > 最可能的種類):
                        最可能的種類 = z+1

                if(種類個數[最可能的種類]==1):
                    三部分最大值= 右耳值
                    最可能 = "右耳"
                    if(左耳值>三部分最大值):
                        三部分最大值 = 左耳值
                        最可能 = "左耳"
                    if(臉值>三部分最大值):
                        三部分最大值 = 臉值
                        最可能 = "臉"
                    最可能的種類 = 三部分結果[最可能]


                if(最可能的種類==正確的種類):
                    正確數+=1

        print("方法2正確率:",float(正確數/測驗總數)*100,"%")
    #------------------------------到此為方法2


    結束時間 = time.time()
    print("執行時間:",結束時間-起始時間,"秒")

if __name__ == '__main__':
    demo(1,"測驗")
    demo(2,"測驗")

    pass
