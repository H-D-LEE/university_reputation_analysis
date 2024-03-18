from senti_module import analyze_sentiments

txt = '커리큘럼 튼튼해요, 교수진 좋은데 수가 적어요, 로스쿨 CPA 고시 금융권 등등 많이 가요, 취업률 높아요, 학과 분위기 쿨해요, 선후배 관계 훈훈해요, 학점 무난해요'
senti_dic = 'Senti_Analysis/Univ_SentiWord.json'

sentiments = analyze_sentiments(txt, senti_dic)
print(sentiments)