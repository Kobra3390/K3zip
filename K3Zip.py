import rich
from rich.console import Console
from rich.progress import track
from function import *

console = Console()

console.print("""[purple]
 ____  __.________ __________.__        
|    |/ _|\_____  \\____    /|__|_____  
|      <    _(__  <  /     / |  \____ \ 
|    |  \  /       \/     /_ |  |  |_> >
|____|__ \/______  /_______ \|__|   __/ 
        \/       \/        \/   |__|    
""")
console.print("[blue]--------------------------------------------------")
console.print("[blue][1]   Extracting File in Zip Archive")
console.print("[blue][2]   Getting all Information About an Archive Zip")
console.print("[blue][3]   Create an Archive Zip")
console.print("[blue][4]   Create an Archive Zip from a Folder")
console.print("[blue]--------------------------------------------------")
console.print("[blue][5]   Create an Archive Tar")
console.print("[blue][6]   Add files to the Tar archive")
console.print("[blue][7]   Check the contents of a Tar archive")
console.print("[blue][8]   Extract files in a folder from a Tar archive")
console.print("[blue][9]   Add a folder to a Tar archive")
console.print("[blue][10]  Check the weight of a file")
console.print("[blue]--------------------------------------------------")
print("\n")

console.print("[purple][ Press Ctrl + C to stop the program ]")

try:
#enter a options
   options = int(input("\n\nEnter a Options: "))
   # analysis of the option
   if(options == 1):
      ExtractingZipFile()
   if(options == 2):
      GettingAllInformationZipFile()
   if(options == 3):
      CreateZipFolder()
   if(options == 4):
      ZipFolder()
   if(options == 5):
      Generate_Tar_Archive()
   if(options == 6):
      Add_File_in_Tar_Archive()
   if(options == 7):
      Check_Contents()
   if(options == 8):
      Extract_In_Folder()
   if(options == 9):
      Add_Folder_Tar_Archive()
   if(options == 10):
      SizeFile()
   if(options > 10):
      console.print("[purple]Invalid Option, exeting...")
except KeyboardInterrupt:
   console.print("\n\n[purple]EXITING....")
except ValueError:
   console.print("\n[purple]Error Value")