#This program will create a batch file given the emulator type and ROM name for a ROM
#that has been downloaded onto user's system

#upgrade GUI
import os
from guizero import App, Text, PushButton, TextBox, Picture, Window
import shutil
import subprocess
#import Image

#ask user for name of game they downloaded
print("What is the name of the game? ")
ROMname = str(input())

#path variables here
print("Please find the path where your emulators are stored: ")
EmulatorLibraryPath =str(input())+"\\"
print("Please find the path where your dolphin executable is stored: ")
DolphinPath = str(input())
##7zip path to be hard set if needed and commented out in line 27
#print("Please find where your 7zip executable is stored: ")
#zippath= str(input([your path]))

#check if user downloaded 7zip
print("Have you downloaded 7zip archive software?")
zipStatus = str(input())
if zipStatus == 'Yes' or zipStatus == 'yes':
    print("Please find where your 7zip executable is stored: ")
    zippath = str(input())
    #continue
else:
    print("7zip software must be installed")
    exit()

######guizero stuff
x = 0
y = 0
def ZipPlacement():
    app.destroy()

######find the file

for f_name in os.listdir(EmulatorLibraryPath):
    if f_name.startswith(ROMname):
            FileToZip = f_name
            print("This is the file you are looking for: " +FileToZip)
            y+=1  #to let me know i found the file and need to break
            break
    else:
        if y == 1:  
            exit()
        else:
            continue

print("What is the name of the console this game is on?")
Console = str(input())

#setting command for cmd
cmd ='"'+zippath+'"'+''+' e '+''+'"'+EmulatorLibraryPath+FileToZip+'" -o"'+DolphinPath+'" *.iso -mx5'

#################section for Gamecube/Wii emulators#########################

if Console =="Gamecube" or Console == "gamecube" or Console== "gameCube" or Console== "GameCube" or Console =="Nintendo Wii" or Console == "wii" or Console== "Wii":
    ####unzipping a file (copy and paste)
    print("Do you wish to unzip this file: " +FileToZip)
    ZipAnswer = str(input())
    if ZipAnswer == "yes":
        if x != 1:
            print('Please copy the following into the open terminal:\n')
            print(cmd)
            subprocess.run(['cmd', '/k', "cd/d "+DolphinPath])
            app = App(title="My Application", height=300, width=200, visible=True)
            button = PushButton(app, text= "Continue", command=ZipPlacement, height="fill", width="fill")
            app.tk.attributes("-fullscreen",True)
            app.show()
            x +=1
            app.display()
        print("Reallocation is complete")
    else:
        #search for next file applicable (if any)
        print("Process ended without zipping")
        ######CANCEL PROGRAM
        exit()
            
    #####renaming the ROM file once it is moved
    z=0
    for f_name in os.listdir(DolphinPath):
        if f_name.startswith(ROMname) and "(USA)" in f_name:
            FileToRename = f_name
            z += 1
            break
        else:
            print("Wasn't extracted here")
            if z==1:
                exit()
            else:
                continue
    old_name = DolphinPath+'\\'+FileToRename
    print("The original name is: "+FileToRename)
    print("What do you want to call it? ")
    new_name = str(input())
    new_name = DolphinPath+'\\'+new_name+'.iso'
    os.rename(old_name, new_name)

    print("What do you want to call the batch file? ")
    batname=str(input())
    gcubefile = open((DolphinPath+'\\'+batname+".bat"), "w+")
    for i in range(1):
        gcubefile.write('"dolphin.exe"' + " " + new_name+ ' --config "Dolphin.Display.Fullscreen=True"')
    gcubefile.close()
    print("Batch file has been created successfully")
    
#####################section for other emulators#######################
else:
    print("The specified Emulator is not recognized")
