# -*- coding: utf-8 -*-
"""
Created on Fri May  3 18:14:17 2024

@author: USER
"""

import sqlite3
import tukorea_scrapy
import suwon_scrapy
import syu_scrapy
import anyang_scrapy
import kumoh_scrapy
import load_reputation
import create_reputation
import insert_reputation

def main() :
    # 대학교 이름과 대응되는 데이터베이스 파일 딕셔너리 생성
    university_databases = {
        "한국공대": "university_reviews_tukorea.db",
        "수원대": "university_reviews_suwon.db",
        "안양대": "university_reviews_anyang.db",
        "금오공대": "university_reviews_kumoh.db",
        "삼육대": "university_reviews_syu.db"
        # 필요한 대학교와 데이터베이스 파일 추가
    }

    # 사용자로부터 대학교 이름 입력 받기
    university_name = input("대학교 이름을 입력하세요: ")

    # 입력된 대학교 이름에 해당하는 데이터베이스 파일명 가져오기
    review_database = university_databases.get(university_name)

    # 해당 대학교 이름에 대한 데이터베이스 파일이 없는 경우 처리
    if not review_database:
        print("해당 대학교에 대한 리뷰 데이터베이스 파일이 없습니다.")
        return
    # 쿼리 실행하여 총 갯수 구하기
    conn = sqlite3.connect(review_database)
    cursor = conn.cursor()
    cursor.execute(f"SELECT MAX(page_num) FROM university_reviews WHERE university_name = '{university_name}'")
    result = cursor.fetchone()[0]
    conn.close()
    
    # start_page 계산
    start_page = int(result) + 1
    last_page = start_page + 10
    
    if university_name == "한국공대" :
        scrapy_university = tukorea_scrapy.scrape_university_reviews(university_name, start_page, last_page)
    elif university_name == "수원대" :
        scrapy_university = suwon_scrapy.scrape_university_reviews(university_name, start_page, last_page)
    elif university_name == "안양대" :
        scrapy_university = anyang_scrapy.scrape_university_reviews(university_name, start_page, last_page)
    elif university_name == "금오공대" :
        scrapy_university = kumoh_scrapy.scrape_university_reviews(university_name, start_page, last_page)
    elif university_name == "삼육대" :
        scrapy_university = syu_scrapy.scrape_university_reviews(university_name, start_page, last_page)
    else:
        print("해당 대학교에 대한 데이터는 존재하지 않습니다.")

    # 데이터베이스 파일명 설정
    combines_database = 'university_reviews_combines.db'
    
    # 데이터베이스에서 대학교 평판과 관련된 리뷰 불러오기
    reputation_reviews = load_reputation.load_reputation_related_reviews(review_database)
    
    # 대학교 평판과 관련된 키워드별로 테이블 생성
    create_reputation.create_tables_for_keywords(combines_database)
    
    # 리뷰를 키워드별로 분류하여 테이블에 삽입
    insert_reputation.insert_reviews_into_keyword_tables(reputation_reviews, review_database, combines_database)
    
if __name__ == "__main__":
    main()