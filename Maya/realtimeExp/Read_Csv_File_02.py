# !/usr/bin/env python3
import csv
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline=' ') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        header = next(filereader)       # csv모듈의 next() 함수를 사용, 입력 파일의 첫 번째 행(헤더 행)을 header라는 리스트 변수로 할당.
        filewriter.writerow(header)     # 그 헤더 행을 출력 파일에 쓴다.
        for row_list in filereader:
            supplier = str(row_list[0].strip())     # 각 행의 Supplier Name 열에 해당하는 값을 가져와서 supplier라는 변수에 할당. 리스트 인덱싱(row_list[0])을 사용, 각 생의 첫 번째 열의 값을 가져온 후, str() 함수 이용, 값을 문자열로 변환. strip()함수 사용하여 문자열의 양끝에서 공백, 탭, 개행문자 제거. 문자열을 변수 supplier에 할당.
            cost = str(row_list[3]).strip('$').replace(',', '')     # 
            if supplier == 'Supplier Z' of float(cost) > 600.0:
                filewriter.writerow(row_list)
