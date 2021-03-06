from zipfile import ZipFile
import datetime
import zipfile
import tarfile
import os
from os.path import basename
import rich
from rich.console import Console

console = Console()

#FUNCTION EXTRACTING ZIP FILE

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
      

#INFORMATION ABOUT ZIP FIL

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


#CREATE A FOLDER .ZIP

def CreateZipFolder():
   path = input("Enter the path where you want to create the .zip folder[at the end of the path there must be the name of the .zip archive]: ")
   path.split("\\")[-1]
   name_folder = path.strip(path)
   FolderZip = zipfile.ZipFile(path, "w")


#CONVERT A ZIP ARCHIVE FROM A FOLDER

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

#CREATE A FOLDER .TAR

def Generate_Tar_Archive():
   #nome dell'archivio in input
   name_tar_archive = input('Enter the name of the TAR archive: ')
	#apertura dell'archivio in modalit?? write
   file = tarfile.open(name_tar_archive, 'w')
	#chiusura dell'archivio
   file.close()

#ADD FILES TO THE TAR ARCHIVE

def Add_File_in_Tar_Archive():
	#lista che conterr?? i file in input
   file_name_list = []
	#nome dell'archivio in input
   name_tar_archive = input('Enter the name of the TAR archive: ')
   while True:
	   #nome dei file in input
      filename = input('Enter a file name you want to add: ')
		#aggiunta dei file in input nella lista
      file_name_list.append(filename)
		#controllo se ci sono altri file da aggiungere
      options = input('Do you want to add other file? Y/N')
      if(options == 'N'):
         break
      print('\n')
	#apertura dell'archivio in modalit?? write
   tar_archive = tarfile.open(name_tar_archive, 'w')
	#inserimento dei file nell'archivio
   for files in file_name_list:
      tar_archive.add(files)
	#chiusura dell'archivio
   tar_archive.close()

#CHECK THE CONTENTS OF A TAR ARCHIVE

def Check_Contents():
	#nome dell'archivio in input
   name_tar_archive = input('Enter the name of the TAR archive: ')
	#apertura dell'archivio in modalit?? lettura
   tar_archive = tarfile.open(name_tar_archive, 'r')
	#controllo dei file nell'archivio col metodo .getnames()
   name_file = tar_archive.getnames()
	#stampa dei file nell'archivio
   print("files in the tar file are:")
   for name in name_file:
      print(name)
	#chiusura dell'archivio
   tar_archive.close()

#Function for extracting files to an output folder

def Extract_In_Folder():
   #nome dell'archivio tar in input
   name_tar_archive = input('Enter the name of the TAR archive: ')
   #nome della cartella di estrazione
   name_folder = input('Enter the name of folder: ')
   #apertura archivio in modalit?? read
   tar_archive = tarfile.open(name_tar_archive, 'r')
   #estrazione
   file_extract = tar_archive.extractall(name_folder)
   #chiusura dell'archivio
   tar_archive.close()

#Add a folder to a Tar archive

def Add_Folder_Tar_Archive():
   name_tar_archive = str(input('Enter the name of the TAR archive: '))
   folder_name = os.path.join(os.getcwd(), str(input("Enter the name of the folder you want to make a tar archive:  ")))
   tar_archive = tarfile.open(f"{name_tar_archive}.tar", 'w')
   directory = os.scandir(folder_name)
   for files in directory:
      os.chdir(folder_name)
      tar_archive.add(name=files.name, recursive=(not files.is_file()))
   tar_archive.close()

#Check the weight of a file

def SizeFile():
   #name of the input file
   name_file = input("Enter the file name: ")
   #calculation in bytes of the file
   file_size = os.path.getsize(name_file)
   #based on the amount of bytes, it prints the different multiples
   if(file_size < 1024):
      console.print(f"File size: [blue]{file_size} Bytes[/blue]")
   elif(file_size > 1024 and file_size < 1048576):
      new_file_size = file_size / 1024
      new_file_size = round(new_file_size, 2)
      console.print(f"File size: [blue]{new_file_size} Kilobytes[/blue]")
   elif(file_size > 1048576 and file_size < 1073741824):
      new_file_size = new_file_size = file_size / 1048576
      new_file_size = round(new_file_size, 2)
      console.print(f"File size: [blue]{new_file_size} Megabytes[/blue]")
   else:
      new_file_size = file_size / 1073741824
      new_file_size = round(new_file_size, 2)
      console.print(f"File size: [blue]{new_file_size} Gigabytes[/blue]")



