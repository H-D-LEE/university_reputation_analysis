from nltk.corpus import sentiwordnet as swn
from nltk.corpus import wordnet as wn
from nltk import pos_tag, word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.sentiment import SentimentIntensityAnalyzer
from konlpy.tag import Kkma
import json
import pandas as pd
import nltk
nltk.download('vader_lexicon')
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('sentiwordnet')

kkma=Kkma()

txt = "하는 만큼 보답받는 대학. 보기에는 건물 몇개 다닥다닥 붙어있는 허접대학 같아도 이만큼 실속있는 배치가 없음. 강의실 옮겨다닐때 그 편안함은... 그리고, 선후배끼리 부조리나 군기는 커녕 그냥 형동생 하는게 더 많고, 부전공 복수전공 열린전공 등등, 자기 과 외의 것들 배우기도 자유로운편.. 다만 저급한 대화를 일삼는 학생 무리가 꽤 있음"   

txt_list=txt.replace(',','.').split('.')
print(txt_list)

with open('SentiWord_info.json', encoding='utf-8-sig', mode='r') as f: 
  SentiWord_info = json.load(f)

senti_dic = pd.DataFrame(SentiWord_info)
senti_dic.set_index('word', inplace=True)
print(senti_dic.head(10))

# 감성 분석 수행
tokens = [kkma.morphs(sentence) for sentence in txt_list]
print(tokens)

df = pd.DataFrame(columns=("review", "sentiment"))
idx = 0
for token in tokens:
    sentiment = 0
    for word in token:
        if word in senti_dic['word_root']:
            sentiment += int(senti_dic.loc[word, 'polarity'])
    df.loc[idx] = [' '.join(token), sentiment]
    idx += 1

result_list=df.values.tolist()
result_dic = {result[0]: result[1] for result in result_list}

print(result_dic)