class Auto() :
    """Eine Klasse für Auto-Objekte"""
    
    def __init__(self, marke: str, typ: str, jahr: int, verbrauch: float) -> None:
        """Initialisierung eines neuen Auto-Objekts"""
        self.marke = marke
        self.typ = typ
        self.jahr = jahr
        self.verbrauch = verbrauch
        self.kmstand = 0.0
        self.reichweite = 0.0
        self.tankvolumen = 60.0
        self.fuellung = 0.0
        
    def zeige(self) -> None :
        """Anzeige der Eigenschaften"""
        print('Km-Stand:', self.kmstand, ' Im Tank:', self.fuellung, 
              'Liter. Reichweite:', self.reichweite, 'km')

    def tanke(self, liter: float) -> None :
        """ Auftanken des Autos erhöht die Tankfüllung bis maximal Tankgrösse"""
        if liter > self.tankvolumen - self.fuellung :
            self.fuellung = self.tankvolumen
        else :
            self.fuellung += liter
        self.reichweite = self.fuellung / self.verbrauch * 100

    def fahre(self, km: float) -> None :
        """Auto fahren für km Kilometer"""
        gefahren = 0.0
        if self.reichweite >= km :
            self.reichweite -= km
            self.kmstand += km
            self.fuellung -= km  / 100 * self.verbrauch
            gefahren = km
        else :
            self.kmstand += self.reichweite
            gefahren = self.reichweite
            self.fuellung = 0.0
            self.reichweite = 0.0
        print('Fahre', gefahren, 'km weit')