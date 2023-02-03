import requests
from bs4 import BeautifulSoup as BS4
from datetime import datetime
# from selenium import webdriver
from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os
import time


# Создаем папку
def create_dir(name_path):
    try:
        os.mkdir(name_path)
    except FileExistsError:
        pass


# Получаем все ссылки
def get_href(file_hrefs):
    with open(f'ALL_H/{file_hrefs}', 'r') as file:
        HREFS = ''.join(file.readlines()).strip().split('\n')

    return HREFS


def create_list(HREFS):
    HREFS_1, HREFS_2 = [], []

    for href in range(0, int(len(HREFS)/2)):
        HREFS_1.append(href)

    for href in range(int(len(HREFS)/2), len(HREFS)+1):
        HREFS_1.append(href)

    return HREFS_1, HREFS_2


