from pydub import AudioSegment
import os, tempfile

def toWAV(old_path, new_path):
    
    sound = AudioSegment.from_file(old_path, "m4a")
    sound.export(new_path, format="wav")
    os.remove(old_path)
    print('old remove ok')
    return new_path