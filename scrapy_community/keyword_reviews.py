# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 21:20:37 2024

@author: USER
"""

import load_reviews
import create_tables
import insert_reviews

def main():
    # 데이터베이스 파일명 설정
    review_database = 'university_reviews_tukorea.db'
    combined_database = 'university_reviews_combined.db'
    
    # 데이터베이스에서 대학교 평판과 관련된 리뷰 불러오기
    reputation_reviews = load_reviews.load_reputation_related_reviews(review_database)
    
    # 대학교 평판과 관련된 키워드별로 테이블 생성
    create_tables.create_tables_for_keywords(combined_database)
    
    # 리뷰를 키워드별로 분류하여 테이블에 삽입
    insert_reviews.insert_reviews_into_keyword_tables(reputation_reviews, review_database, combined_database)

if __name__ == "__main__":
    main()
