print("星际rep自动下载,因为国服很坑,只有极少部分rep可以看,但是我仍然坚持学习.所以就需要写一个爬虫大量下载然后找能看的学习!!!!!!!!!")





dizhi="https://lotv.spawningtool.com/zip/?query=&amp;coop=&amp;patch=&amp;pro_only=on&amp;after_played_on=&amp;after_time=&amp;order_by=play&amp;before_played_on=&amp;before_time=&amp;p="



#引用 requests文件
import requests



#外国网下载慢,等着即可.一个包大概6mb左右.
for i in range(1,10): #============下载999页#设置好需要下多少页,然后就会每一页下载一个zip包.
     #下载地址
     Download_addres=dizhi+str(i)
     #把下载地址发送给requests模块
     f=requests.get(Download_addres)
     #下载文件
     with open(f"{i}.zip","wb") as code:
          code.write(f.content)
     print("finish one zip")









