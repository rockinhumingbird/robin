
from urllib.request import urlopen as uReq

my_url = 'https://www.vox.com/a/sexual-harassment-assault-allegations-list'

from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
uClient = uReq(my_url)
pagehtml = uClient.read()
uClient.close()
soup=soup(pagehtml,'html.parser')
soup.p

nameList1 = soup.findAll('div',{'class': 'col'})

for name in nameList1:
    print(name.get_text())

f = open("C:\\Users\\Richard\\zoe.txt", 'w')
for name in nameList1:
	f.write(name.get_text())
	f.write(',')
f.close()


accusation = soup.main.findAll('div',{'class': 'info-body'})
for name in accusation:
    print(name.get_text())

f = open("C:\\Users\\Richard\\accusation.txt", 'w')
for name in accusation:
	f.write(name.get_text())
	f.write(',')
f.close()

quote = soup.main.findAll('blockquote')
for name in quote:
    print(name.get_text())

f = open("C:\\Users\\Richard\\quote1.txt", 'w')
for name in quote:
	f.write(name.get_text())
	f.write(',')
f.close()


from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html, "html.parser")
nameList = bs.findAll('span', {'class': 'green'})
for name in nameList:
    print(name.get_text())
for name in nameList:
    print(name.get_text())
while(True):
    if request == 'GET':
        if distributed_queue.size()>0:
            send(distributed_queue.get())
        else:
            break
    elif request == 'POST':
        bf.put(my_url)



def count_words_at_url(my_url):
    """Just an example function that's called async."""
    resp = requests.get(url)
    return len(resp.text.split())    


from redis import Redis
from rq import Queue

q = Queue(connection=Redis())
from my_module import count_words_at_url
job = q.enqueue(count_words_at_url)
def count_words_at_url(url):
    """Just an example function that's called async."""
    resp = requests.get(url)
    return len(resp.text.split())