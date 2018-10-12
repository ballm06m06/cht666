import psycopg2
from cht_package.config import db,user,pwd,host,dbport


def register_User(id, name, picUrl):
    try:
        conn = psycopg2.connect(database = db, user = user, 
                                        password = pwd, host = host, port=dbport)
        print('Opened DB successfully')
        cur = conn.cursor()
        cur.execute("INSERT INTO chtUser (ID,NAME,PicUrl)  VALUES (%s, %s, %s )", (id, name, picUrl))
        conn.commit()
        print('%s註冊成功'%(name))
        conn.close()
        return True

    except Exception as e:
        print('register exception:' + str(e))
        return False