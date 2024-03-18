# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 15:54:42 2024

@author: USER
"""

import requests
import sqlite3
from bs4 import BeautifulSoup
from urllib.request import urlopen
import datetime

def scrape_university_reviews(university_name):
    base_url = 'https://gall.dcinside.com/board/lists?id=kpu'
    response = requests.get(base_url)

    if response.status_code == 200:
        url = urlopen(base_url).read()
        print(url)
        soup = BeautifulSoup(urlopen(base_url).read(), 'html.parser')
        save_to_database(university_name, soup)
    else:
        print(f"Error: {response.status_code}")

def save_to_database(university_name, soup):
    conn = sqlite3.connect('university_reviews.db')
    cursor = conn.cursor()
    table_div = soup.find('table', class_='gall_list')
    print(soup)
    print(table_div)
    #cursor.execute('''CREATE TABLE IF NOT EXISTS university_reviews (university_name TEXT, review_title TEXT, review_content TEXT, date TEXT)''')
    #tables = table_div.find_all("tr")
    #trs = tables.find_all('tr')
    #titles = soup.find_all('td', class_='title')
    #contents = soup.find_all('div', class_='content')
    #dates = soup.find_all('span', class_='date')
    # print(trs)
    #data_to_save = []
   # for title, content, date in zip(titles, contents, dates):
    #    title_text = title.get_text(strip=True)
   #     # 대학교 이름이 제목에 있는지 확인하고 해당하는 경우에만 데이터에 추가
   #     if university_name in title_text:
   #         content_text = content.get_text(strip=True)
   #         date_str = date.get_text(strip=True)
   #         data_to_save.append((university_name, title_text, content_text, date_str))

    #cursor.executemany("INSERT INTO university_reviews VALUES (?, ?, ?, ?)", data_to_save)
    conn.commit()

    conn.close()

def main():
    university_name = input("대학교 이름을 입력하세요: ")
    scrape_university_reviews(university_name)

if __name__ == "__main__":
    main()