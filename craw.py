#!/usr/bin/env python3
from bs4 import BeautifulSoup  # 网页解析模块
import requests  # 网络请求模块
import csv  # csv 文件模块
import time
import lxml


def craw(pages=5, name='bj'):
    # 网址
    if name == 'hf':
        url = "https://{name}.58.com/pinpaigongyu/pn/{page}/?minprice=1000_2000"
    else:
        url = "https://{name}.58.com/pinpaigongyu/pn/{page}/?minprice=2000_4000"

    # 伪造头部请求
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.37'
    }

    # 初始化页码
    page = 0
    # 打开rent.csv文件，如果没有就创建一个，并设置写入模式
    csv_file = open("rent.csv", "w", encoding="utf-8")
    # 创建writer对象
    csv_writer = csv.writer(csv_file, delimiter=',')
    # 循环所有页面
    while True:
        if page == pages:
            break
        page += 1
        print("fetch: ", url.format(page=page, name=name))
        time.sleep(1)
        # 抓取目标页面
        response = requests.get(url.format(page=page, name=name), headers=headers)
        # 设置编码模式
        response.encoding = 'utf-8'
        # 创建一个BeautifulSoup对象，获取页面正文
        html = BeautifulSoup(response.text, features="lxml")
        # 获取当前页面的房子信息
        house_list = html.select(".list > li")

        # 循环在读不到新的房源时结束
        if not house_list:
            break
        # 房子信息
        for house in house_list:
            # 获取房子标题
            house_title = house.select("h2")[0].string
            # 获取房子链接地址
            house_url = house.select("a")[0]["href"]
            # 对标题进行分隔
            house_info_list = house_title.split()
            # 如果第二列是公寓名则取第一列作为地址
            if "公寓" in house_info_list[1] or "青年社区" in house_info_list[1]:
                house_location = house_info_list[0]
            else:
                house_location = house_info_list[1]

            house_money = house.select(".money")[0].select("b")[0].string
            # 写入一行数据
            csv_writer.writerow([house_title, house_location, house_money, house_url])
            # 关闭文件
    csv_file.close()

