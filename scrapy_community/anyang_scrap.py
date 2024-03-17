# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 16:23:56 2024

@author: USER
"""
import time
import requests
from bs4 import BeautifulSoup
import sqlite3

def scrape_university_reviews(university_name):
    base_url = 'https://gall.dcinside.com/board/view/?id=anyang_university&no={}'  # {}에는 게시물 번호가 들어갈 자리입니다.
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36'}
    
    
    page_num = 23800
    while True:
        url = base_url.format(page_num)
        response = requests.get(url, headers=headers)
    
        #if response.status_code != 200:
        #    break
        print(url)
        # 페이지의 HTML을 파싱합니다.
        soup = BeautifulSoup(response.content, 'html.parser')
        #print(soup)

        # 대학교 이름이 포함된 게시글만 스크래핑하여 데이터베이스에 저장합니다.
        save_to_database(university_name, soup)

        page_num += 1
        #print(page_num)
        if page_num == 23801 :
            break
        time.sleep(3)  # 3초 대기 후 다음 페이지로 이동합니다.

def save_to_database(university_name, soup):
    conn = sqlite3.connect('university_reviews_anyang.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS university_reviews (university_name TEXT, review_title TEXT, review_content TEXT, date TEXT)''')

    # 게시물 제목과 내용에서 대학교 이름이 포함되어 있는지 확인합니다.
    titles = soup.select(".ub-word > .title_subject")
    contents = soup.select(".write_div > p")
    dates = soup.select(".gall_date")
    #print(titles)
    #print(contents)
    data_to_save = []
    
    # titles와 contents의 길이 중 작은 값을 기준으로 반복합니다.
    min_length = min(len(titles), len(contents))
    for i in range(min_length):
        title = titles[i].text.strip()
        content = contents[i].text.strip()
        date = dates[i]['title'].strip()
        #print("제목:", title)
        #print("내용:", content)
        data_to_save.append((university_name, title, content, date))

    cursor.executemany("INSERT INTO university_reviews (university_name, review_title, review_content, date) VALUES (?, ?, ?, ?)", data_to_save)
    conn.commit()
    conn.close()

def main():
    university_name = input("대학교 이름을 입력하세요: ")
    scrape_university_reviews(university_name)

if __name__ == "__main__":
    main()
