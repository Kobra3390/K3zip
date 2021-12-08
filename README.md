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

---
# K3Zip Versione 2 "K3Zip V2" (IT)

Nella versione 2 di K3Zip sono state aggiunge diverse funzionalitá inerenti agli Archivi Tar, ben 6 funzioni che si vanno aggiungere alle giá 4 presenti, esse sono:

5. __Crea un archivio Tar__: Con tale funzione andiamo a creare un Archivio Tar dando in input il nome dell'archivio
6. __Aggiungi file all'Archivio Tar__: Con questa funzione andiamo ad aggiungere file ad un Archivio Tar creato in precedenza, i file dovranno trovarsi nella stessa directory del programma, o dovrá essere inserito per esteso il loro percorso di sistema
7. __Controllare il contenuto di un archivio Tar__: Con questa formula si va a controllare il contenuto di un Archvio Tar, in output ci restituirá nome di file e cartelle presenti nell'archivio.
8. __Estrai i file in una cartella da un archivio Tar__: Questa operazione va a estrarre in una cartella di output tutto il contenuto di un archivio Tar
9. __Aggiungi una cartella a un archivio Tar__: Con questa funzione andiamo ad aggiungere una cartella (contenente file ed eventuali altre sottocartelle) ad un Archivio Tar
10. __Controlla il peso di un file__: Con questa funzionalitá é possibile sapere il peso di un certo file con annessi i suoi multipli e sottomultipli (KiloBytes, MegaBytes, GigaBytes etc)

---
# K3zip Version 2 "K3Zip V2" 

In K3Zip version 2 some functionalities inherent to Tar Archives have been added, 6 of them to be exact:

5. __Create a Tar Archive__: With this funciton the user can create a Tar Archive, by giving the archive's name in input.

6. __Add a file to a Tar Archive__: With this funciton we can add a file to the previously created archive; the file must be in the same directory as the program, otherwise the full file path needs to be entered.

7. __Check the content of a Tar Archive__: with this funciton we can check the names of files and folders contained in the archive.

8. __Extract files from a Tar Archive__: with this operation, all the files in the archive get extracted in an output folder.

9. __Add a folder in a Tar Archive__: this funciton adds a folder(and subfolders and files contained in it, if present) to a Tar Archive.

10. __Check a file's size__: with this functionality it's possible to know a file's size, in Kilobytes, Megabytes, Gigabytes and their multiples/submultiples.
