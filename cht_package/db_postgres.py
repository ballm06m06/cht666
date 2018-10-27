import psycopg2
from cht_package.config import db,user,pwd,host,dbport

#註冊
def register_User(id, name, picUrl, areaCode, notify):
    try:
        conn = psycopg2.connect(database = db, user = user, 
                                        password = pwd, host = host, port=dbport)
        print('Opened DB successfully')
        cur = conn.cursor()
        cur.execute("INSERT INTO chtUser (ID,NAME,PicUrl,areaCode,notify)  VALUES (%s, %s, %s, %s, %s)", (id, name, picUrl,areaCode,notify))
        conn.commit()
        print('%s註冊成功'%(name))
        conn.close()
        return True

    except Exception as e:
        print('register exception:' + str(e))
        return False

def user_notify_open(mid):
    try:
        conn = psycopg2.connect(database = db, user = user, 
                                        password = pwd, host = host, port=dbport)
        print('Opened DB successfully')
        cur = conn.cursor()
        cur.execute("UPDATE chtUser SET isNotify = '1' WHERE id = %s",(mid,))
       
        conn.close()
        return True

    except Exception as e:
        print('exception:' + str(e))
        return False

def user_notify_close(mid):
    try:
        conn = psycopg2.connect(database = db, user = user, 
                                        password = pwd, host = host, port=dbport)
        print('Opened DB successfully')
        cur = conn.cursor()
        cur.execute("UPDATE chtUser SET isNotify = '0' WHERE id = %s",(mid,))
        conn.commit()
        conn.close()
        return True

    except Exception as e:
        print('exception:' + str(e))
        return False

def user_notify_query(id):
    try:
        conn = psycopg2.connect(database = db, user = user, 
                                        password = pwd, host = host, port=dbport)
        print('Opened DB successfully')
        cur = conn.cursor()
        print('Opened database successfully')
        cur = conn.cursor()

        cur.execute("SELECT isNotify from chtUser WHERE ID = (%s)", (id))
        rows = cur.fetchall()

        print(rows)
        conn.close()

    except Exception as e:
        print('exception:' + str(e))
        return False