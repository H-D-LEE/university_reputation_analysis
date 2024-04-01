import senti_module as st
import db_con as db


senti_dic = 'Senti_Analysis/Univ_SentiWord.json'
scrap_db = 'Senti_Analysis/university_reviews_combines.db'
senti_db = 'Senti_Analysis/senti2.db'

def stop_while_analyzing(conn, keyword):
    print(f"분석 종료. 현재 DB에 저장된 {keyword} 테이블 개수 : {db.db_table_count(conn, keyword)}개")
    exit()
    
def pn_classificate(polarity):
    if polarity <-5:
        return '매우 부정'
    elif -5<=polarity<-1:
        return '부정'
    elif -1<=polarity<=1:
        return '중립'
    elif 1<polarity<=5:
        return '긍정'
    else:
        return '매우 긍정'

if __name__ == "__main__":
    
    scrap_conn= db.db_conn(scrap_db)
    senti_conn= db.db_conn(senti_db)
    
    keyword=''
    while True:
        keyword=input('''분석을 진행할 키워드명을 입력하세요.\n
                    1. 교과 2. 교수 3. 등록금 4. 복지 5. 비교과 6. 시설 7. 진로 8. 중단(q)\n
                    >>> ''')
        if keyword not in ['교과', '교수', '등록금', '복지', '비교과', '시설', '진로', 'q']:
            print('다시 입력하세요.')
            continue
        if keyword=='q':
            print('프로그램을 종료합니다.')
            exit()
        else:
            break
    data=db.db_fetch_non_limit(scrap_conn, keyword)

    if data:
        print(f"테이블 {len(data)}개 발견. {keyword} 키워드에 대한 분석 시작.")
        for row in data:
            if len(row[2])>3000:
                continue
            #print(row[0])
            if '실시간' in row[1] or '현재상황' in row[1] or '현재 상황' in row[1]:
                continue
            txt, result = st.analyze_sentiments(row[2], senti_dic)
            if bool(result):
                cum_polarity=0
                print(result)
                print(result.values())
                for i in range(len(result)):
                    cum_polarity+=list(result.values())[i]
                print(f"문장: {txt}")
                print(f'문장 극성 합계: {cum_polarity} - 문장 긍부정 결과 : {pn_classificate(cum_polarity)}')
                db.db_insert(senti_conn, keyword, row[0], row[2], row[3], pn_classificate(cum_polarity))
    print(f"분석 종료. 현재 DB에 저장된 {keyword} 테이블 개수 : {db.db_table_count(senti_conn, keyword)}개")
    db.db_close(scrap_conn)
    db.db_close(senti_conn)