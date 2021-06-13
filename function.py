from zipfile import ZipFile
import datetime
import zipfile
import os
from os.path import basename

"""FUNCTION EXTRACTING ZIP FILE"""

def ExtractingZipFile():
   # specifying the zip file name in input
   name_folder = input("Enter a name folder .zip: ")
   print("\n")
   # confirmation of the name in input
   confirmation = input(f"A name file is: {name_folder}, Y / N: ")
   print("\n")
   if(confirmation == 'y' or confirmation == 'Y'):
      with ZipFile(name_folder, 'r') as zip:
         # printing all the contents of the zip file
         zip.printdir()

         # extracting all the files
         print('Extracting all the files now...')
         zip.extractall()
         print('Done!')
   if(confirmation == 'n' or confirmation == 'N'):
      print("Sorry, you entered the file name wrong")
      
#--------------------------------------------------------------------------

"""INFORMATION ABOUT ZIP FILE"""

def GettingAllInformationZipFile():
   # specifying the zip file name in input
   name_folder = input("Enter a name folder .zip: ")
   print("\n")
   # confirmation of the name in input
   confirmation = input(f"A name file is: {name_folder}, Y / N: ")
   print("\n")
   if(confirmation == 'y' or confirmation == 'Y'):
      with ZipFile(name_folder, 'r') as zip:
         for info in zip.infolist():
            print(info.filename)
            print('\tModified:\t' + str(datetime.datetime(*info.date_time)))
            print('\tSystem:\t\t' + str(info.create_system) + '(0 = Windows, 3 = Unix)')
            print('\tZIP version:\t' + str(info.create_version))
            print('\tCompressed:\t' + str(info.compress_size) + ' bytes')
            print('\tUncompressed:\t' + str(info.file_size) + ' bytes')
   if(confirmation == 'n' or confirmation == 'N'):
      print("Sorry, you entered the file name wrong")

#--------------------------------------------------------------------------

"""CREATE A FOLDER .ZIP"""

def CreateZipFolder():
   path = input("Enter the path where you want to create the .zip folder[at the end of the path there must be the name of the .zip archive]: ")
   path.split("\\")[-1]
   name_folder = path.strip(path)
   FolderZip = zipfile.ZipFile(path, "w")

#--------------------------------------------------------------------------

"""CONVERT A ZIP ARCHIVE FROM A FOLDER"""

def ZipFolder():
   name_folder = input("Enter a name folder: ")
   confirmation = input(f"A name folder is: {name_folder}, Y / N: ")
   print("\n")
   if(confirmation == 'y' or confirmation == 'Y'):
      with ZipFile('K3Zip.zip', 'w') as K3:
         for folderName, subfolders, filenames in os.walk(name_folder):
            for filename in filenames:
               #create complete filepath of file in directory
               filePath = os.path.join(folderName, filename)
               # Add file to zip
               K3.write(filePath, basename(filePath))
   if(confirmation == 'n' or confirmation == 'N'):
      print("Sorry, you entered the file name wrong")
