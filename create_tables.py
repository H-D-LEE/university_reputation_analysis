# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 21:12:57 2024

@author: USER
"""

import sqlite3

def create_tables_for_keywords(database_name='university_reviews_combined.db'):
    # 대학교 평판과 관련된 단어 목록
    reputation_keywords = ['대학교', '학교', '학생', '교수', '수업', '등록금', '장학금']
    
    # 데이터베이스 연결
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    
    # 대학교 이름이 들어가는 테이블 생성
    cursor.execute('''CREATE TABLE IF NOT EXISTS university_names (
                        university_name TEXT,
                        review_title TEXT,
                        review_content TEXT,
                        date TEXT)''')
    
    # 각 키워드별로 테이블 생성
    for keyword in reputation_keywords:
        cursor.execute(f'''CREATE TABLE IF NOT EXISTS {keyword} (
                            university_name TEXT,
                            review_title TEXT,
                            review_content TEXT,
                            date TEXT)''')
    
    # 연결 종료
    conn.close()
