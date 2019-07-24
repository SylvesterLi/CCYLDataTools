import jieba
import wordcloud

w=wordcloud.WordCloud()
w.generate("py and ppp")
w.to_file("pic.png")
print('success!!!')
