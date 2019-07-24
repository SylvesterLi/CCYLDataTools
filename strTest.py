from datetime import datetime

i=5
xp='//*[@id="Pl_Official_MyProfileFeed__25"]/div/div[%s]/div[2]/div/ul/li[1]/a/span/span/i'



print('//*[@id="Pl_Official_MyProfileFeed__25"]/div/div[%d]/div[2]/div/ul/li[1]/a/span/span/i' % i)
print('hello-%s-%d' % (datetime.now(),i))