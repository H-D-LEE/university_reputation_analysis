import sqlite3

def db_conn(db_path):	
    try:
        conn = sqlite3.connect(db_path)
        print('db 연결 완료')
        return conn
    except sqlite3.Error as e:
        print("db 연결 오류:", e)
        return None
    
def db_fetch(conn, keyword, univ_name, num):
    try:
        cursor = conn.cursor()
        query = f"SELECT review_content, date FROM {keyword} WHERE university_name = ? ORDER BY date DESC LIMIT ?"
        cursor.execute(query, (univ_name, num))
        rows = cursor.fetchall()
        return rows
    except sqlite3.Error as e:
        print("db fetch 오류:", e)
        return None

def db_fetch_non_limit(conn, keyword):
    try:
        cursor = conn.cursor()
        query = f"SELECT * FROM {keyword} ORDER BY date DESC"
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows
    except sqlite3.Error as e:
        print("db fetch 오류:", e)
        return None
    
def db_table_count(conn, keyword):
    try:
        cursor = conn.cursor()
        query = f"SELECT count(*) FROM {keyword}"
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows
    except sqlite3.Error as e:
        print("db table count 오류:", e)
        return None
    
def db_close(conn):
    try:
        conn.close()
        print("db 연결 해제 완료")
    except sqlite3.Error as e:
        print("db 연결 해제 오류:", e)
        
def db_insert(conn, keyword, univ, txt, date, result):
    try:
        cursor = conn.cursor()
        query = f"INSERT or ignore into {keyword} values(?, ?, ?, ?)"
        cursor.execute(query, (univ, txt, date, result))
        print("db 레코드 삽입 완료")
        conn.commit()
    except sqlite3.Error as e:
        print("db 레코드 삽입 오류:", e)