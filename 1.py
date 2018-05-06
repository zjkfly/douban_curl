import requests
import re
def write_to_file(filename,name):
    f = open(filename,'a')
    for title in name:
        f.writelines(title+'\n')
    f.close()
def get_title(count):
    url = 'https://movie.douban.com/top250?start='+str(count)+'&filter='
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'}
    r = requests.get(url,headers = headers)
    title = re.findall(r'<span class="title">(.*?)</span>',r.text)
    #过滤其他版本的名称
    for i in range(len(title)):
        if title[len(title)-i-1].find('&nbsp')!=-1:
            del title[len(title)-i-1]
    print(title)
    return title
for count in range(250):
    if count%25==0:
        write_to_file('movie250.txt', get_title(count))
