import os
import csv
import sys


def read_csv():
    file = os.path.join(os.getcwd(), 'data-398-2018-08-30.csv')
    print(file)
    with open(file, mode='r', encoding='utf-8') as f:
        read_file = csv.DictReader(f, delimiter=',')
        my_list = []
        for i in read_file:
            my_list.append(i)
    return my_list


read_csv()