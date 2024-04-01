import sqlite3

db='Senti_Analysis/senti2.db'
conn=sqlite3.connect(db)
c=conn.cursor()

""" test 테이블 생성""" 

c.execute('''CREATE TABLE 진로
            (university_name TEXT,
                review_content TEXT,
                date TEXT,
                result TEXT)''')
conn.commit()
conn.close()



""" test 테이블에서 데이터 삽입, 조회
name='A'
c.execute("insert into test (name) values (?)", (name))

conn.commit()

c.execute("select * from test")

result = c.fetchone()
if result:
    print(result)
else:
    print("없음")
    
conn.close()

"""