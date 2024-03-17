import json 
class Senti():
    def data_list(wordname):	
            with open('data/SentiWord_info.json', encoding='utf-8-sig', mode='r') as f:
                data = json.load(f)
            result = ['None','None']	
            for entry in data:
                if entry['word'] == wordname:
                    result = [entry['word_root'], entry['polarity']]
                    break
                
            r_word = result[0]
            s_word = result[1]	
            
            return r_word, s_word