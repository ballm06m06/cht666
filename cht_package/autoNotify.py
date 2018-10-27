from bot.cht_sensor import get_do_value, get_ph_value, get_tmp_value
from cht_package.db_postgres import user_notify_query
from datetime import datetime
import time




# 每n秒执行一次
def timer(n):
    while True:
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        time.sleep(n)
# 5s
timer(5)