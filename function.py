from zipfile import ZipFile

def ExtractingZipFile():
   # specifying the zip file name in input
   name_folder = input("Enter a name folder .zip: ")
   # confirmation of the name in input
   confirmation = input(f"A name file is {name_folder} Y / N: ")
   if((confirmation == 'y') or (confirmation == 'Y')):
      with ZipFile(name_folder, 'r') as zip:
         # printing all the contents of the zip file
         zip.printdir()

         # extracting all the files
         print('Extracting all the files now...')
         zip.extractall()
         print('Done!')
