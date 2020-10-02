##imports ##
import os,sys



#getting cwd

cwd=os.getcwd()

print(f"folder : {cwd}\n\n")



#listing files and removing

lis= os.listdir()

if lis==["organizer.py"]:

 print(f"No files found in folder : {os.getcwd()}")

 sys.exit()

lis.remove("organizer.py")

files=lis.copy()



class main:

 def __init__(self):
  self.path=os.getcwd()
  

 def getext(self,ext_name):

  exts=[fil for fil in files if os.path.splitext(fil)[1].lower() in ext_name]

  return exts

	

 def create_if_not(self,folder):

     if not os.path.exists(folder):

      os.makedirs(folder)

	

 def move(self,foldername,filee):

      for fil in filee:          

          os.replace(fil,f"{cwd}/{foldername}/{fil}")

    





#===creating folders===#

print("=========================================")

print("Defining folder's")



main.create_if_not("python_Images")

main.create_if_not("python_Docs")

main.create_if_not("python_Pdf")

main.create_if_not("python_Video")

main.create_if_not("python_Audio")

main.create_if_not("python_Others")



#=====extentions======#

print("=========================================")

print("Getting files extentions")



img_ext=[".jpg",".png",".jpeg"]

docs_ext=[".txt",".doc",".docx",".csv",".xlsx",".md"]

pdf_ext=[".pdf"]

video_ext=[".mp4",".avi",".mkv",".3gp",".mkv"]

audio_ext=[".mp3",".flv",".mpeg",".ogg",".wav"]



#=====classificatipn of files=====#

print("=========================================")

print("Classifing files according to extensions")



images=main.getext(img_ext)

docs=main.getext(docs_ext)

pdf=main.getext(pdf_ext)

video=main.getext(video_ext)

audio=main.getext(audio_ext)

other=[]



#=====appeding files=====#

for fil in files:

     ext=os.path.splitext(fil)[1].lower()

     if (ext not in img_ext) and (ext not in docs_ext) and (ext not in pdf_ext) and (ext not in video_ext) and (ext not in audio_ext) and os.path.isfile(fil):

         other.append(fil) 



#====moving files=====#

print("=========================================")

print("Moving files according to extensions")



main.move("python_Images",images)

main.move("python_Docs",docs)

main.move("python_Pdf",pdf)

main.move("python_Video",video)

main.move("python_Audio",audio)

main.move("python_Others",other)





#=====running class======#

print("=========================================")

print("Task Successed")
#running class
run=main()
