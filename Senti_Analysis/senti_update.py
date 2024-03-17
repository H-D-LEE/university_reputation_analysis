import json
def load_sentiment_dictionary(file_path):
    with open(file_path, encoding='utf-8-sig', mode='r') as f:
        return json.load(f)

def save_sentiment_dictionary(data, file_path):
    with open(file_path, encoding='utf-8-sig', mode='w') as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=4)

def update_sentiment_dictionary():
    data = load_sentiment_dictionary('SentiWord_info.json')
    
    print("감성 사전 Update 프로그램입니다.")
    print("사전에 단어가 없는 경우, 입력한 정보 대로 추가되며")
    print("사전에 단어가 이미 있는 경우, 덮어쓸지 말지 결정할 수 있습니다.")
    print("종료는 단어 입력칸에 #를 입력하세요.\n")

    while True:
        word = input("단어 : ").strip()

        # 종료 입력 시 반복문 탈출
        if word == '#':
            save_sentiment_dictionary(data, 'SentiWord_info.json')
            print("프로그램을 종료합니다.")
            break

        # 한글이 아닌 단어 입력 시 문구 출력 후 재입력
        if not word.isalpha() or not all('ㄱ' <= c <= '힣' for c in word):
            print("한글 단어만 입력하세요.")
            continue

        word_root = input("단어의 어근 : ").strip()

        # 한글이 아닌 단어 입력 시 문구 출력 후 재입력
        if not word_root.isalpha() or not all('ㄱ' <= c <= '힣' for c in word_root):
            print("올바른 한글 어근을 입력하세요.")
            continue

        word_polarity = input(" 극성 점수 (-2: 매우 부정 / -1: 부정 / 0: 중립 / 1: 긍정 / 2: 매우 긍정): ").strip()
        # -2, -1, 0, 1, 2 중 하나의 숫자가 아닌 문자 입력 시 문구 출력 후 재입력
        if word_polarity not in ['-2', '-1', '0', '1', '2']:
            print("극성 점수는 -2, -1, 0, 1, 2 중 하나의 숫자만 입력하세요.")
            continue
        
        applied = False
        
        for entry in data:
            
            if entry['word'] == word:
                print("이미 사전에 등록된 단어입니다.")
                print(f"사전 정보: word: {entry['word']}, word_root: {entry['word_root']}, polarity: {entry['polarity']}")
                print(f"변경될 정보: word: {word}, word_root: {word_root}, word_polarity: {word_polarity})")
                while True:
                    answer = input("입력 정보 확인 후, 변경 사항을 적용하려면 Y, 취소 후 재입력하려면 N을 눌러 주세요.").strip()
                    if answer in ['y', 'Y']:
                        entry['word_root'] = word_root
                        entry['polarity'] = word_polarity
                        print("변경 완료되었습니다.")
                        applied = True
                        break
                    elif answer in ['N', 'n']:
                        print("변경 취소되었습니다.")
                        applied = True
                        break
                    else:
                        print("입력 오류.")
                        continue
            if applied:
                break
        
        if not applied:
            print(f"추가될 정보: word: {word}, word_root: {word_root}, word_polarity: {word_polarity})")
            while True:
                answer = input("입력 정보 확인 후, 사전에 등록하려면 Y, 취소 후 재입력하려면 N을 눌러 주세요.").strip()
                if answer in ['y', 'Y']:
                    data.append({
                        "word": word,
                        "word_root": word_root,
                        "polarity": word_polarity
                    })
                    print("추가 완료되었습니다.")
                    applied = True
                    break
                elif answer in ['N', 'n']:
                    print("추가 취소되었습니다.")
                    applied = True
                    break
                else:
                    print("입력 오류.")
                    continue
                
        if not applied:
            print("오류로 인해 업데이트 작업이 제대로 완료되지 않았습니다. ")

if __name__ == "__main__":
    update_sentiment_dictionary()