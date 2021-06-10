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
print("\n")

#enter a options
options = int(input("Enter a Options: "))

# analysis of the option
if(options == 1):
   ExtractingZipFile()

