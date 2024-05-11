import senti_module as st
import db_con as db
import log_management as log
import keyboard
import threading

class Hook(threading.Thread):
    def __init__(self):
        super(Hook, self).__init__()  # parent class __init__ 실행
        self.daemon = True  # 데몬쓰레드로 설정
        self.event = False  # f4가 눌리면 event 발생
        keyboard.unhook_all()  # 후킹 초기화
        keyboard.add_hotkey('-', print, args=['\n- pressed'])  # -가 눌리면 print 실행
        
    def run(self):  # run method override
        print('Hooking Started')
        while True:
            key = keyboard.read_hotkey(suppress=False)  # hotkey를 계속 읽음
            if key == '-':  # - 받은 경우
                self.event = True # event 클래스 변수를 True로 설정
                print("- 눌림")
                stop_and_save(log_json, log_file[list(log_file.keys())[0]])
                print(f"분석 중단. 프로그램을 종료합니다.")
                exit()  # 반복문 탈출
            
senti_dic = 'Senti_Analysis/Univ_SentiWord.json'
scrap_db = 'Senti_Analysis/university_reviews_combines.db'
senti_db = 'Senti_Analysis/senti2.db'
log_json = 'Senti_Analysis/task_counts.json'

    
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
    
def stop_and_save(log_json, key_counts):
    j=log.load_log(log_json)
    log.write_log(j, key_counts)
    log.save_log(log_json, j)
    

if __name__ == "__main__":
    
    
    
    h = Hook()  # 훅 쓰레드 생성
    h.start()  # 쓰레드 실행
    
    while True:

        keyword=input('''분석을 시작하려면 y를 누르세요. q을 누르면 종료됩니다. \n
                    >>> ''')
        if keyword not in ['y', 'q']:
            print('다시 입력하세요.')
            continue
        if keyword=='q':
            print('프로그램을 종료합니다.')
            exit()
        elif keyword=='y':
            scrap_conn= db.db_conn(scrap_db)
            senti_conn= db.db_conn(senti_db)
            log_file=log.load_log(log_json)[-1]
            print(log_file)
            print('분석을 시작합니다. 분석을 중지하려면 - 를 누르세요. ')

            key_list=['교과', '교수', '등록금', '복지', '비교과', '시설', '진로']
            key_counts=log_file[list(log_file.keys())[0]]
            for key in key_list:
                data=db.db_fetch_non_limit(scrap_conn, key, log_file[list(log_file.keys())[0]][key]-1000)
                if data:
                    print(f"테이블 {len(data)}개 발견. {key} 키워드에 대한 분석 시작.")
                    for row in data:
                        if h.event==True:
                            exit()
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
                            db.db_insert(senti_conn, key, row[0], row[2], row[3], pn_classificate(cum_polarity))
                        key_counts[key]+=1
                print(f"{key} 분석 종료. 현재 DB에 저장된 {key} 테이블 개수 : {db.db_table_count(senti_conn, key)}개")
                    
    