"""kwargs_demo.py demonstriert den Aufruf einer 
Funktion mit Schlüsselwort-Argumenten"""

def doppel( liste: list, zahl: int) -> list :
    for element in liste:
        print(element * zahl)

l = [2, 3, 4]

# Aufruf mit den Namen der Parameter
doppel( zahl=2, liste=l )

