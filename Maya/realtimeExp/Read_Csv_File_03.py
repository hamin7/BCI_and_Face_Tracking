import csv

line_counter = 0
header = []
customer_list = []

with open('csv_file.csv') as f:
    while 1:
        data = f.readline().replace("\n","")    # 줄바꿈기호 하나 제거.
        print(data)     # data에 파일을 한 줄씩 불러옴.
        if not data: break
        if line_counter == 0:
            header = data.split(",")    # 맨 첫 줄은 header로 저장.
        else:
            customer_list.append(data.split(","))
        line_counter += 1
