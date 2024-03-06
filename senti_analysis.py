from kss import split_sentences
from nltk.corpus import sentiwordnet as swn
from nltk.corpus import wordnet as wn
from nltk import pos_tag, word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.sentiment import SentimentIntensityAnalyzer
from konlpy.tag import Okt
import json
import pandas as pd
import nltk
nltk.download('vader_lexicon')
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('sentiwordnet')


txt = "하는 만큼 보답받는 대학. 보기에는 건물 몇개 다닥다닥 붙어있는 허접대학 같아도 이만큼 실속있는 배치가 없음. 강의실 옮겨다닐때 그 편안함은... 그리고, 선후배끼리 부조리나 군기는 커녕 그냥 형동생 하는게 더 많고, 부전공 복수전공 열린전공 등등, 자기 과 외의 것들 배우기도 자유로운편.. "   

txt_list=split_sentences(txt)

with open('SentiWord_info.json', encoding='utf-8-sig', mode='r') as f: 
  SentiWord_info = json.load(f)

custom_sentiment_dictionary = pd.DataFrame(SentiWord_info)

# 감성 사전 업데이트 함수
def update_sentiment_dictionary(word, pos, score, sentiment_dictionary):
    if pos == 'a':
        sentiment_dictionary[word] = score
    elif pos == 'v':
        sentiment_dictionary[word] = score
    elif pos == 'r':
        sentiment_dictionary[word] = score
    elif pos == 'n':
        sentiment_dictionary[word] = score
# 감성 사전 업데이트
update_sentiment_dictionary('저급한', 'a', -0.5, custom_sentiment_dictionary)
score_list = []



# 감성 분석 수행
okt = Okt()
tokens = [okt.morphs(txt)]
tokens = list(map(lambda x : " ".join(x), tokens))
print(tokens)
df = pd.DataFrame(columns=("review", "sentiment"))
idx = 0
for token in tokens:                                
  sentiment = 0                                    
  for i in range(0, len(custom_sentiment_dictionary)):           
    if custom_sentiment_dictionary.word[i] in token:              
      sentiment += int(custom_sentiment_dictionary.polarity[i])   
  df.loc[idx] = [token, sentiment]                  
  idx += 1

result_list=df.values.tolist()
result_dic={}
for i in range(len(result_list)):
   result_dic[result_list[i][0]]=result_list[i][1]

print(result_dic)