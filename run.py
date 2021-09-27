from video_to_faces import video_to_faces
import os

if __name__ == '__main__':
    print('current working path: ', os.getcwd())
    while 1:
        inp = input('Path to video: ')
        while 1:
            if inp == 'exit':
                exit()
            if os.path.isfile(inp):
                break
            else:
                inp = input('Please enter a valid path: ')
        
        path = inp

        inp = input('Extract eyes? [y/n] ')
        eyes = 0
        while 1:
            if inp == 'exit':
                exit()
            if inp == 'y' or inp == 'Y' or inp == 'yes' or inp == 'Yes' or inp == 'YES':
                eyes = True
                break
            elif inp == 'n' or inp == 'N' or inp == 'no' or inp == 'No' or inp == 'NO':
                eyes = False
                break
            else:
                inp = input('Extract eyes? [y/n] ')

        video_to_faces(path, eyes=eyes)
        
