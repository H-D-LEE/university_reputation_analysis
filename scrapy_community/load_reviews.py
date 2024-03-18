# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 21:16:32 2024

@author: USER
"""

import sqlite3

def load_reputation_related_reviews(database_name='university_reviews_tukorea.db'):
    # 대학교 평판과 관련된 단어 목록
    reputation_keywords = ['대학교', '학교', '학생', '교수', '수업', '등록금', '장학금']
    
    # 데이터베이스 연결
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    
    # 쿼리 생성
    query = "SELECT DISTINCT university_name, review_title, review_content, date FROM university_reviews"
    
    # 대학교 평판과 관련된 단어가 포함된 리뷰를 검색하여 가져오기
    reputation_reviews = []
    for row in cursor.execute(query):
        matched_keywords = [keyword for keyword in reputation_keywords if keyword in row[2]]
        if len(matched_keywords) >= 1:  # 1개 이상의 키워드가 매치된 경우에만 추가
            reputation_reviews.append(row)
    
    # 중복 제거
    reputation_reviews = list(set(reputation_reviews))
    
    # 연결 종료
    conn.close()
    
    return reputation_reviews
