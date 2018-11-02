
import gevent
from gevent import monkey
monkey.patch_all()    #执行脚步插件修改阻塞行为
from socket import *


#　创建套接字
def server():
    s = socket()
    s.bind(("0.0.0.0",2505))
    s.listen(5)
    while True:
        c,addr = s.accept()
        print("Connect from",addr)
        # handler(c)  # 循环方案
        gevent.spawn(handler,c)  #协程方案

def handler(c):
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b"Receive message")
    c.close()

