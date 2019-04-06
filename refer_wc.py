import jieba as jb
import itertools
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator


#定义文件位置
word_list = dict()
ciyun_data = open('H:\data\wordcloud\ciyun.csv','r', encoding='UTF-8')    #避免GBK解码错误
stop_word = open('H:\data\wordcloud\stopword.txt','r')
stop_word_list = [x.rstrip() for x in stop_word.readlines()]


#处理数据格式
for line in itertools.islice(ciyun_data,1,None):                #跳过第一行
    sentence_total = line.rstrip().split('\t')[1]               #取出所有推荐理由的句子 eg:["口感很好,很划算","价格实惠,速度快","超好吃的,鸡排简直好吃","很实在啊直接给了一罐可乐","好吃实惠,可乐是罐装的百事"]
    value_num =  int(float(line.rstrip().split('\t')[-1]))
    for phrase in sentence_total.split('"'):                    #按"分割成对应的短语LIST
        if phrase != '[' and phrase != ']' and phrase != ',' :  #短语不等于[ , ] 等符号就用结巴开始分词
            words = (list(set(jb.cut(phrase))))
            for word in words:
                if word != ',' :
                   word_list[word] = word_list.get(word,0) + value_num    #生成word对应次数出现的字典

#删除无意义的停顿词
for key in list(word_list.keys()) :
    if key in stop_word_list :
        word_list.pop(key)



#开始制作词云
cloud_mask = np.array(Image.open("H:\data\wordcloud\eleme.jpg"))
backgroud_Image = plt.imread("H:\data\wordcloud\eleme.jpg")
img_colors = ImageColorGenerator(backgroud_Image)                           #使用背景图片的色系
wc = WordCloud(background_color= 'white',mask = cloud_mask,font_path = 'C:\Windows\Fonts\simhei.ttf',max_words=50000)
wc.generate_from_frequencies(word_list)
#wc.recolor(color_func=img_colors)
wc.to_file('H:\data\wordcloud\wc_50000.jpg')





