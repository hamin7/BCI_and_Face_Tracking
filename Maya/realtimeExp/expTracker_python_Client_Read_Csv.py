import os
import socket
import subprocess
import csv

header = []
customer_list = []

s = socket.socket()
host = '166.104.29.148'
port = 7777
s.connect((host,port))

with open('csv_file.csv') as f:
    while True:
        data = f.readline().replace("\n","").encode('utf-8')    # 줄바꿈 기호 하나 제거.
        # print("send: ", data)
        # Val = imput("send: ").encode()
        s.send(data)
        if not data:
            break

s.close()
