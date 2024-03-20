import json
import kss
from konlpy.tag import Okt

class Senti():
    def __init__(self, dic_file):
        self.dic_file = dic_file

    def data_list(self, wordname):	
        with open(self.dic_file, encoding='utf-8-sig', mode='r') as f:
            data = json.load(f)
        result = ['None','None']	
        for entry in data:
            if entry['word'] == wordname:
                result = [entry['word'], entry['polarity']]
                break
                
        word = result[0]
        pol = result[1]	
            
        return word, pol

def analyze_sentiments(txt, senti_dic):
    okt = Okt()
    senti = Senti(senti_dic)
    sentiments = {}
    sentences = kss.split_sentences(txt)

    for sentence in sentences:
        sentiment = 0
        tokens = okt.morphs(sentence, stem=True)
        pre_neg = False
        pre_word = [0, 0]
        w_count=0
        for i, word in enumerate(tokens):
            #print('{0: <10}'.format(i), '{0: <10}'.format(word), end='')
            w, word_polarity = senti.data_list(word)
            if w != 'None':
                w_count+=1
                #print(f'극성 존재 - {w},{word_polarity}')
                if pre_neg==True:
                    #print('관형사 부정으로 무효')
                    pre_neg=False
                    continue
                else:
                    sentiment += int(word_polarity)
                pre_word=[w, int(word_polarity)]
            elif i > 0 and tokens[i] in ['있다', '하다']: 
                #print(f' - 긍정으로 인해 {pre_word[0]}의 극성 유효')
                pre_word=[0,0]
            elif i > 0 and tokens[i] in ['않다', '없다', '아니다', '커녕']: 
                if tokens[i-1]=='별로':
                    continue
                #print(f' - 부정으로 인해 {pre_word[0]}의 극성 무효')
                sentiment -= pre_word[1]
            elif i > 0 and tokens[i] in ['많다']: 
                #print(f' - 강조로 인해 {pre_word[0]}의 극성 강화')
                sentiment -= pre_word[1]*1.5
            elif i > 0 and tokens[i] in ['적다']: 
                #print(f' - 부정 강조로 인해 {pre_word[0]}의 극성 약화')
                sentiment -= pre_word[1]*0.5
            elif tokens[i] in ['안', '못']:
                #print(f' - 부정으로 인해 이어지는 단어의 극성 무효')
                pre_neg=True
            #else:
                #print(f'누적 극성: {sentiment}')
        if w_count==0:
            continue
        sentiments[sentence.strip().replace(' ','')] = sentiment
        
    return (txt, sentiments)