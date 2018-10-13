from pydub import AudioSegment
import os, tempfile
from os import walk

static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')


def toWAV(old_path, new_path):
    print(old_path+ ' '+ new_path)
    sound = AudioSegment.from_file(old_path, "m4a")
    sound.export(new_path, format="wav")
    os.remove(old_path)
    print('old audio file remove ok')

    for root, dirs, files in walk(static_tmp_path):
        print("路徑：", root)
        print("  目錄：", dirs)
        print("  檔案：", files)

    return new_path
