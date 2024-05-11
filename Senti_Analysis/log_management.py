import json
from datetime import datetime
task_counts= {
                '교과': 11649,
                '교수': 4094,
                '등록금': 2440,
                '복지': 4477,
                '비교과': 1745,
                '시설': 5268,
                '진로': 2556
            }

def load_log(log_file):
    with open(log_file, encoding='utf-8-sig', mode='r') as f:
        return json.load(f)
    
def save_log(log_file, data):
    with open(log_file, encoding='utf-8-sig', mode='w') as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=4)
        
def write_log(j, cur_counts):
    # 현재 시각을 문자열로 변환
    cur_time = datetime.now().strftime("%m-%d %H:%M:%S")

    # 현재 시각을 키로 가지는 딕셔너리 생성
    data = {cur_time: cur_counts}

    # JSON 파일에 저장
    j.append(data)
    print(f"로그 파일 저장 완료. {cur_time}")
        
        