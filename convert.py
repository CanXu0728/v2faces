import os
from pathlib import Path

def convert(path):
    path = str(path)
    save_path = path.replace('.h264', '.mp4')
    try:
        os.system('ffmpeg -loglevel quiet -i ' + path + ' ' + save_path)
        print('complete converting ', path)
    except:
        print('error occured, skip ', path)

def main():
    list_h264 = Path('./videos').rglob('*.h264')
    for path in list_h264:
        convert(path)
    print('='*30)
    print('complete')

if __name__ == '__main__':
    main()