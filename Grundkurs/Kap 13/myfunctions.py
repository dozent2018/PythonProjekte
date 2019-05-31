# myfunctions.py enthält nützliche Funktionsdefinitionen
def is_int(string) :
    try:
        zahl = int(string)
        return True
    except ValueError:
        return False

def read_int(prompt) :
    while is_int == False :
        try:
            zahl = int(input(prompt))
            return ist_zahl
        except ValueError:
            print("Die Eingabe ist keine ganze Zahl")
