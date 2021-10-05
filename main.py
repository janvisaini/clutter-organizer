import os
import sys

# defining extensions
img=[".jpg",".png",".jpeg",".svg",".tiff"]
docs=[".txt",".doc",".docx",".csv",".xlsx",".md"]
pdf=[".pdf"]
video=[".mp4",".avi",".mkv",".3gp",".mkv",".mov",".flv",".f4v"]
audio=[".mp3",".flv",".mpeg",".ogg",".wav"]

# move the file to d)f location
def move(from_ ,to):
    os.replace(from_, to)

#get the extension of file
def get_extension(file):
    return os.path.splitext(file)[-1]

#create directory provided in list
def create_dir(directory,dirs):
    for dir in dirs:
        if not os.path.exists(os.path.join(directory,dir)):
            os.mkdir(os.path.join(directory,dir))

path = input("Enter the path to organize: ")

# validation of path
if not os.path.exists(path):
    print("Path doesn't exist")
    sys.exit(0)

#get content in the directory and filter it only if it is a file
items = [x for x in os.listdir(path) if os.path.isfile(os.path.join(path,x))]

create_dir(path,['Images','Videos','Docs','Audios','Pdfs','Others'])

#cleaning of clutter
for item in items:
    ext = get_extension(item)
    # maping ext with name
    classification = {
        'Images':img,
        'Videos':video,
        'Docs':docs,
        'Audios':audio
        ,'Pdfs':pdf,
    }

    for key,value in classification.items():
        if ext in value:
            # moving the files             
            move(os.path.join(path,item),os.path.join(path,f"{key}/{item}"))
            break
        
# checking any file remaining and moving it to others
for item in items:
    if os.file.exists(os.path.join(path,item)):
        move(os.path.join(path,item),os.path.join(path,f"Others/{item}"))
        
        
        
    

