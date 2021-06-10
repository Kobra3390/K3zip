from zipfile import ZipFile
import datetime

"""FUNCTION EXTRACTING ZIP FILE"""

def ExtractingZipFile():
   # specifying the zip file name in input
   name_folder = input("Enter a name folder .zip: ")
   print("\n")
   # confirmation of the name in input
   confirmation = input(f"A name file is {name_folder} Y / N: ")
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
      print("sorry, you entered the file name wrong")
      
#--------------------------------------------------------------------------

"""INFORMATION ABOUT ZIP FILE"""

def GettingAllInformationZipFile():
   # specifying the zip file name in input
   name_folder = input("Enter a name folder .zip: ")
   print("\n")
   # confirmation of the name in input
   confirmation = input(f"A name file is {name_folder} Y / N: ")
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

#--------------------------------------------------------------------------

