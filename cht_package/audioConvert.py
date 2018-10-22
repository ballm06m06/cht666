from pydub import AudioSegment
import os, tempfile
from os import listdir
from os.path import isfile, isdir, join

static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')


def toWAV(old_path, new_path):
    #print(old_path+ ' '+ new_path)
    sound = AudioSegment.from_file(old_path, "m4a")
    sound.export(new_path, format="wav")
    os.remove(old_path)
    print('.m4a audio file remove ok')

    print('查看/static/tmp...')
    # 取得所有檔案與子目錄名稱
    files = listdir('static/tmp')
    # 以迴圈處理
    for f in files:
        # 產生檔案的絕對路徑
        fullpath = join('static/tmp', f)
        # 判斷 fullpath 是檔案還是目錄
        if isfile(fullpath):
            print("檔案：", f)
        elif isdir(fullpath):
            print("目錄：", f)

    return new_path
