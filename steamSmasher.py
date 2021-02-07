import os
import pathlib

def stopDownloads(path):
    print("killing automatic downloads in " + path)
    for filename in os.listdir(path):
        if("appmanifest" in filename):
            print(pathlib.Path(path + "\\" + filename))
            f = open(pathlib.Path(path + "\\" + filename), "rt")
            
            file = f.read()

            file = file.replace('"AutoUpdateBehavior"		"0"','"AutoUpdateBehavior"		"1"')

            f.close()
            
            f = open(pathlib.Path(path + "\\" + filename), "wt")

            f.write(file)

            f.close


stopDownloads(os.path.dirname(os.path.realpath(__file__)))
    
f = open("libraryfolders.vdf", "r")
libraryfile = f.readlines()

for line in libraryfile:
    line = line.replace(" ","")
    line = line.replace("   ","")
    line = line.replace('"',"")
    
    if(len(line) > 4):

        if(line[4].isupper()):
            print("Found library on drive: " + line[4])

            librarypath = ""

            i = 4
            while(not line[i].isspace()):
                
                librarypath += line[i]
                i += 1
            librarypath = librarypath + "\steamapps"
            #print(librarypath)
            stopDownloads(librarypath)


