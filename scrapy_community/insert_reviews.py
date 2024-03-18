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
                # 해당 키워드 테이블에 이미 데이터가 있는지 확인
                cursor.execute(f"SELECT * FROM {keyword} WHERE review_title=? OR review_content=?", (review[1], review[2]))
                existing_data = cursor.fetchone()
                if not existing_data and review[2] != '':  # 이미 데이터가 존재하지 않는 경우에만 삽입
                    cursor.execute(f"INSERT INTO {keyword} VALUES (?, ?, ?, ?)", (review[0], review[1], review[2], review[3]))
                    
    # 변경사항 저장 및 연결 종료
    conn.commit()
    conn.close()