import rich
from rich.console import Console
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

console.print("[1] Extracting a zip file")
console.print("[2] Getting all information about a zip file")
console.print("[3] Create a Folder .zip")
print("\n")

#enter a options
options = int(input("Enter a Options: "))

# analysis of the option
if(options == 1):
   ExtractingZipFile()
if(options == 2):
   GettingAllInformationZipFile()
if(options == 3):
   CreateZipFolder()
