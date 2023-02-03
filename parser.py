import requests
from bs4 import BeautifulSoup as BS4
from datetime import datetime
# from selenium import webdriver
from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os
import time
import modules_parser
from multiprocessing import Process


HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0'}


def main():
    dir_path = os.path.dirname(os.path.abspath(__file__))

    session_path = os.path.join(dir_path, 'Session')
    # session_path = os.path.join(dir_path, 'Ulvi')

    options = webdriver.ChromeOptions()
    # options.
    options.add_experimental_option("excludeSwitches", ['enable-automation'])
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_argument(f"--user-data-dir={session_path}")
    options.add_argument('--profile-directory=Profile 1')
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument(f'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0')

    proxy = {
        "proxy": {
            "https": "http://feemuZ:fY8Z0v@107.152.152.243:8000"
        }
    }

    ALL_files_hrefs = os.listdir('ALL_H/')


    with webdriver.Chrome(ChromeDriverManager().install(), options=options, seleniumwire_options=proxy) as driver:

        for file_hrefs in ALL_files_hrefs[16::]:
            print(file_hrefs)

            name_path = f"READY/{file_hrefs.split('_')[-1].split('.txt')[0]}"

            # Создаем папку
            modules_parser.create_dir(name_path)

            # Получаем все ссылки
            HREFS = modules_parser.get_href(file_hrefs)

            HREFS_1, HREFS_2 = modules_parser.create_list(HREFS)

            # p1 = Process(target=save, args=(HREFS_1, name_path, options, proxy,))
            # p2 = Process(target=save, args=(HREFS_2, name_path,))
            # p1.start()
            # p2.start()

            # p1.join()
            # p2.join()

            # with webdriver.Chrome(ChromeDriverManager().install(), options=options, seleniumwire_options=proxy) as driver:
            for href in HREFS[0::]:
                if f'{href.split("skuId=")[-1]}.html' not in os.listdir(f'{name_path}'):
                    while True:
                        print(href)
                        try:
                            driver.get(href)
                            # driver.find_element('xpath', '/html/body/div[2]/div/div/div/div[1]/div[2]/a[2]').click()
                            # time.sleep(5)
                            page = driver.page_source

                            with open(f'{name_path}/{href.split("skuId=")[-1]}.html', 'w', encoding='utf-8') as file:
                                file.write(page)
                            break
                        except:
                            pass


def save(HREFS, name_path):
    dir_path = os.path.dirname(os.path.abspath(__file__))

    session_path = os.path.join(dir_path, 'Session')
    # session_path = os.path.join(dir_path, 'Ulvi')

    options = webdriver.ChromeOptions()
    # options.
    options.add_experimental_option("excludeSwitches", ['enable-automation'])
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_argument(f"--user-data-dir={session_path}")
    options.add_argument('--profile-directory=Profile 1')
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument(f'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0')

    proxy = {
        "proxy": {
            "https": "http://feemuZ:fY8Z0v@107.152.152.243:8000"
        }
    }

    with webdriver.Chrome(ChromeDriverManager().install(), options=options, seleniumwire_options=proxy) as driver:
        for href in HREFS[0::]:
            print(href)
            driver.get(href)

            page = driver.page_source

            with open(f'{name_path}/{href.split("skuId=")[-1]}.html', 'w', encoding='utf-8') as file:
                file.write(page)




if __name__ == '__main__':
    main()


