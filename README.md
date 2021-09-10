# Introduzione a K3Zip (IT)
K3Zip è un semplice script scritto interamente in python (nella versione 3.9.2), che sfrutta il modulo *zipfile* e la programmazione funzionale. K3Zip permette di semplicare tutte quelle operazione sugli *archivi .zip*.
Il progretto è formato da due file: 
`K3Zip.py` e `function.py`. In `function.py` sono presenti tutte le funzioni che permettono le varie operazione che lo script può effettuare, il file `K3Zip.py` è il file `main` del progetto in cui vengono richiamate tutte le funzioni di `function.py`. 

---
# Introduction an K3Zip (EN) 
K3Zip is a simple script written entirely in python, that uses the *zipfile module* and functional programming. It is made up of two files: `K3Zip.py` and `function.py`, the first is the main file of the project, the second contains all the functions recalled in the main file. 

---
# Requisiti (IT)
__Windows__: Avere la versione più aggiornata del interprete python (minimo dalla 3.9.2 in poi), stessa cosa per quanto riguarda __Linux__. Avere inoltre anche il modulo `rich` installato:
```python
$ pip install rich
```

---
# Requirements (EN)
__Windows__: Must have python interpreter 3.9.2 or newer, same thing for __Linux__. Also have the `rich` module installated:
```python
$ pip install rich
```

---
# Installazione (IT)
Windows e Linux: 
```
$ git clone https://github.com/Kobra3390/K3zip.git
$ cd K3Zip
$ python K3Zip.py 
```
Per Linux l'ultimo comando può essere anche:
```
$ python3 K3Zip.py
```

---
# Hot to Install (EN)
Windows and Linux:
```
$ git clone https://github.com/Kobra3390/K3zip.git
$ cd K3Zip
$ python K3Zip.py 
```
(The last command could be "python3 K3Zip.py" for Linux)

---
# Caratteristiche (IT)
K3Zip ha 4 funzionalità principali:

1. __Estrarre file da un archivio zip__: Questa funzione permette l'estrazione di file e cartelle da un archivizio .zip, l'archizio si dovrà trovare nella stessa cartella di `K3Zip.py`.

1. __Estrazione Informazioni da un file zip__: Questa funzione permette di conoscere le informazioni legate all'archivio come: file che contiene, il loro peso da archiviati e da compressi. L'archivzio si dovrà contenere nella stessa cartella dello script.

1. __Creazione Archivizio Zip__: Questo funzione permette di creare un archivio zip specificando il percorso dove crearlo, *attenzione* alla fine del percorso dovrà essere specificato il nome dell'archivizio .zip.

1. __Convertire una cartella in un archivio zip__: Questa funzione permette di trasformare una cartella in un archivio zip. La cartella da convertire dovrà essere nella stessa cartella dello script.

---
# Features (EN)
K3Zip has four possible operations:

1. __Extraction of files from a .zip archive__: This operation allows the extraction of files and folders from a zip archive. the archive must be in the same folder as the script

1. __Extraction of informations from a zip file__: This operation gives various info about the files inside of a zip archive, such as the file's extension, the size of the file, zipped and unzipped. The archive must be in the same folder as the script

1. __Creation of a zip archive__: This operation creates a zip archive, by specifing the path where it should be created The name of the archive goes at the end of the path specification

1. __Convertion of a folder in a zip archive__: This operation allows the user to turn a folder in a zip archive. The folder must be in the same folder as the script
