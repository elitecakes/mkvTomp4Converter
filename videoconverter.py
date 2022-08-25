import os
import ffmpeg ##run pip install ffmpeg-python 
              ##NOT JUST FFMPEG IT WONT WORK OTHERWISE
import shutil

def main():
    print("let's get started now shall we\n")

    currentDir = os.getcwd()
    ##mkvDir = os.path.join(currentDir, "mkvfiles")
    ##mp4Dir = os.path.join(currentDir, "mp4files")
    
    mkvDir = input("Input directory of .mkv file folder: ")
    mp4Dir = input("Input directory of .mp4 file folder: ")

    print(currentDir)
    print(mkvDir)
    print(mp4Dir)

#    if (continueOrNot() == False):
#        return
    
    for path, folder, files in os.walk(mkvDir):
        for file in files:

            if file.endswith('.mp4'):
                print("Found mp4 file: %s" % file)
#                if (continueOrNot() == False):
#                    continue
                move_to_mp4_folder(file, mkvDir, mp4Dir)
            
            elif file.endswith('.mkv'):
                print("Found file: %s" % file)
 #               if (continueOrNot() == False):
#                    continue
                namemp4 = convert_to_mp4(os.path.join(mkvDir, file))
                move_to_mp4_folder(namemp4, mkvDir, mp4Dir)

            else:
                pass
    
def convert_to_mp4(mkv_file):
    name, ext = os.path.splitext(mkv_file)
    out_name = name + ".mp4"
    ffmpeg.input(mkv_file).output(out_name).run()
    print("Finished converting {}".format(mkv_file))
    return out_name

def continueOrNot():
    yn = input('\n1 to convert this file 0 to skip to next file: ')
    if (yn == 1):
        return True
    else:
        return False

def move_to_mp4_folder(file, mkvDir, mp4Dir):
    filepathTrue = os.path.join(mkvDir, file)
    shutil.move(filepathTrue, mp4Dir)# + "/" + file)
    print("moved " + file +"\n")








if __name__ == "__main__":
    main()
