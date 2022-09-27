from ast import Return
from pickle import FALSE, NONE, TRUE
from PIL import Image
from datetime import datetime
import sys

from xmlrpc.client import boolean

from numpy import append

class Nota:
    def __init__(self, memo, date, tags):
        self.memo= memo
        self.date=date
        self.tags=tags
    def getMemo(self):
        return self.memo
    def getDate(self):
        return self.date 
    def getTags(self):
        return self.tags
    def toString(self):
        strn= "Nota: {self.memo} / data: {self.date}"
        return strn
    """
    def match(self,filter):
        print("Busca per la etiqueta: ")
        if (self.tags==filter):
            search(self)
            return TRUE
        else:
            return FALSE
    
    """
       

class Notebook():
    
    def __init__(self):
        self.notes=[]
 
    def search(self):
        print("Cerca per etiqueta :")
        lista=[]
        filter = input()
        for note in self.notes:
            tags=note.getTags()
            if (tags==filter):
                a=note.getMemo()
                b=note.getDate()
                lista.append(f"Nota: {a} / data: {b} / hastag: {tags}")
        for ob in lista:
            print(ob)

    def new_note(self,memo,tags):
        date_in = datetime.now().strftime("%H:%M:%S")
        self.notes.append(Nota(memo,date_in,tags)) 
    
    def see(self):
        for note in self.notes:
            print(note.memo) 
        

class Main():
    llibreta = Notebook()
    menus=TRUE
    def menu():

        print()
        print("")
    while menus == TRUE:
        choice = input("""************ - Benivingut a Notebook - **************
                    1: Mostrar dades
                    2: Buscar
                    3: Afegir
                    4: Sortir

                    Selecciona una opció: """)

        if choice == "1" or choice ==1:
            llibreta.see()
        elif choice == "2" or choice ==2:
            llibreta.search()
        elif choice=="3" or choice==3:
            print("Escriu la teva nota")
            memo_in=input()
            print("Escriu el hastag")
            tags_in=input()
            llibreta.new_note(memo_in,tags_in)
        elif choice=="4" or choice==4:
            menus= NONE
            sys.exit
        else:
            print("Sols pots elegir una de les opcions")
            print("Torna a provar")
    
    
    
    
