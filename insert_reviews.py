# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 21:14:44 2024

@author: USER
"""

import sqlite3

def insert_reviews_into_keyword_tables(reviews, university_name, database_name='university_reviews_combined.db'):
    # 대학교 평판과 관련된 단어 목록
    reputation_keywords = ['대학교', '학교', '학생', '교수', '수업', '등록금', '장학금']
    
    # 데이터베이스 연결
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    
    # 리뷰를 키워드별로 분류하여 테이블에 삽입
    for review in reviews:
        matched_keywords = [keyword for keyword in reputation_keywords if keyword in review[2]]
        if len(matched_keywords) >= 1:  # 1개 이상의 키워드가 매치된 경우에만 처리
            for keyword in matched_keywords:
                cursor.execute(f"INSERT INTO {keyword} VALUES (?, ?, ?, ?)", review)
        # 대학교 이름이 들어가는 테이블에도 리뷰 삽입
        cursor.execute("INSERT INTO university_names VALUES (?, ?, ?, ?)", (university_name,) + review[1:])
    
    # 변경사항 저장 및 연결 종료
    conn.commit()
    conn.close()
