import psycopg2
from cht_package.config import db,user,pwd,host,dbport

#註冊
def register_User(id, name, picUrl, areaCode):
    try:
        conn = psycopg2.connect(database = db, user = user, 
                                        password = pwd, host = host, port=dbport)
        print('Opened DB successfully')
        cur = conn.cursor()
        cur.execute("INSERT INTO chtUser (ID,NAME,PicUrl,areaCode)  VALUES (%s, %s, %s, %d)", (id, name, picUrl,areaCode))
        conn.commit()
        print('%s註冊成功'%(name))
        conn.close()
        return True

    except Exception as e:
        print('register exception:' + str(e))
        return False