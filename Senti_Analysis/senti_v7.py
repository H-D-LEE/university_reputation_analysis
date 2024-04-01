import senti_module as st
import db_con as db

senti_dic = 'Senti_Analysis/Univ_SentiWord.json'
scrap_db = 'Senti_Analysis/university_reviews_combines.db'
senti_db = 'Senti_Analysis/senti2.db'

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
    
    univ_name=input('''감성 분석을 진행할 대학명을 입력하세요\n
                   1. 한국공대 2. 수원대 3. 강남대 4. 안양대 5. 금오공대\n
                   >>> ''')
    if univ_name not in ['한국공대', '수원대', '강남대', '안양대', '금오공대']:
        print('다시 입력하세요.')
        exit()
    keyword=input('''분석을 진행할 키워드명을 입력하세요.\n
                  1. 교수 2. 대학교 3. 등록금 4. 수업 5. 장학금 6. 학교 7. 학생\n
                  >>> ''')
    if keyword not in ['교수', '대학교', '등록금', '수업', '장학금', '학교', '학생']:
        print('다시 입력하세요.')
        exit()
    num=int(input("분석을 진행할 레코드 개수를 입력하세요: "))
    data=db.db_fetch(scrap_conn, keyword, univ_name, num)
    if data:
        for row in data:
            #print(row[0])
            if '실시간' in row[2] or '현재상황' in row[2] or '현재 상황' in row[2]:
                continue
            txt, result = st.analyze_sentiments(row[0], senti_dic)
            if bool(result):
                cum_polarity=0
                print(result)
                print(result.values())
                for i in range(len(result)):
                    cum_polarity+=list(result.values())[i]
                print(f"문장: {txt}")
                print(f'문장 극성 합계: {cum_polarity} - 문장 긍부정 결과 : {pn_classificate(cum_polarity)}')
                db.db_insert(senti_conn, keyword, univ_name, row[0], row[1], pn_classificate(cum_polarity))
    db.db_close(scrap_conn)
    db.db_close(senti_conn)