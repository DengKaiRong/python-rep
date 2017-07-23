# coding=utf-8
import urllib
import re

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'"hoverURL":"(.+?)"'
    imgre = re.compile(reg)
    imageslist = re.findall(imgre,html)

    # 处理转义字符
    resultImgList = []
    for imgurl in imageslist:
        newImg = imgurl.replace('\\','')
        resultImgList.append(newImg)
    return resultImgList

html = getHtml("http://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1500656012281_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E5%81%9A%E7%88%B1")

fo = open("web.html", "wb")
fo.write(html)
fo.close()

# 保存图片地址
imgList = getImg(html)
print '结果' + '\n'.join(imgList)

fo = open("result.txt","wb")
str_convert = '\n'.join(imgList)
fo.write(str_convert)
fo.close()

# 下载资源
x = 0
for imgurl in imgList:
    print '正在下载: ' + imgurl
    urllib.urlretrieve(imgurl,"img/%s.jpg" % x)
    print '完成'
    x+=1

# print html