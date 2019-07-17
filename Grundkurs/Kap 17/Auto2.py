class Auto() :
    """Eine Klasse für jede Art von Autos
    """
    def __init__(self, marke: str, typ: str, jahr: int) -> None:
        """Initialisierung eines neuen Auto-Objekts. Enhält nur Attribute, 
        die für alle Arten von Autos gelten"""
        self.marke = marke
        self.typ = typ
        self.jahr = jahr
        self.kmstand = 0.0
        self.reichweite = 0.0

    def zeige(self) -> None :
        """Anzeige der Eigenschaften"""
        print('Marke:', self.marke, 'Typ:', self.typ, 
              'Baujahr:', self.jahr, 'Km-Stand:', self.kmstand)

    def fahre(self, km: float) -> None :
        if km >= self.reichweite :
            gefahren = self.reichweite
        else :
            gefahren = km
            self.reichweite -= km
        print(gefahren, 'km gefahren.') 


class VerbrennerAuto(Auto):
    """Ist von der allgemeinen Klasse Auto abgeleitet"""
    def __init__(self, marke: str, typ: str, jahr: int, tank: float, verbrauch: float) -> None:
        """Initialisierung eines neuen VerbrennerAuto-Objekts. Benutzt zunächst die 
        __init__ Funktion von Auto, dann werden die Attribute gesetzt, die für ein
        VerbrennerAuto zusätzlich benötigt werden"""
        super().__init__(marke, typ, jahr)
        # Maximaler Tankinhalt
        self.tankvolumen = tank
        self.fuellung = 0.0
        # Kraftstoffverbrauch auf 100 km
        self.verbrauch = verbrauch

    def zeige(self) -> None :
        """Anzeige der Eigenschaften, zuerst die Eigenschaften der Oberklasse, dann die
        Eigenschaften der Unterklasse"""
        super().zeige()
        print(' Im Tank:', self.fuellung, 'Liter. Reichweite:', self.reichweite, 'km')

    def tanke(self, liter: float) -> None :
        """ Auftanken des Autos erhöht die Tankfüllung bis maximal Tankgrösse"""
        if liter > self.tankvolumen - self.fuellung :
            self.fuellung = self.tankvolumen
        else :
            self.fuellung += liter
        self.reichweite = self.fuellung / self.verbrauch * 100

    def fahre(self, km: float) -> None :
        """Auto fahren für km Kilometer mit Verbrennungsmotor"""
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

class ElektroAuto(Auto):
    """Ist von der allgemeinen Klasse Auto abgeleitet"""
    def __init__(self, marke: str, typ: str, jahr: int, kwh: float, verbrauch: float) -> None:
        """Initialisierung eines neuen ElektroAuto-Objekts. Benutzt zunächst die 
        __init__ Funktion von Auto, dann werden die Attribute gesetzt, die für ein
        ElektroAuto zusätzlich benötigt werden"""
        super().__init__(marke, typ, jahr)
        # Lade-Kapazität Batterie in Kilowattstunden
        self.batterie_kap = kwh
        # Ladezustand Batterie in Kilowattstunden
        self.ladung = 0.0
        # Verbrauch in Kilowattstunden pro 100 km
        self.verbrauch = verbrauch

    def zeige(self) -> None :
        """Anzeige der Eigenschaften, zuerst die Eigenschaften der Oberklasse, dann die
        Eigenschaften der Unterklasse"""
        super().zeige()
        print(' Batterieladung:', self.ladung, 'kWh. Reichweite:', self.reichweite, 'km')

    def lade(self, kwh: float) -> None :
        """Laden der Batterie erhöht den Ladestand und die Reichweite"""
        if kwh > self.batterie_kap - self.ladung :
            self.ladung = self.batterie_kap
        else :
            self.ladung += kwh
        self.reichweite = self.ladung / self.verbrauch * 100

    def fahre(self, km: float) -> None :
        """Auto fahren für km Kilometer mit Elektromotor"""
        gefahren = 0.0
        if self.reichweite >= km :
            self.reichweite -= km
            self.kmstand += km
            self.ladung -= km  / 100 * self.verbrauch
            gefahren = km
        else :
            self.kmstand += self.reichweite
            gefahren = self.reichweite
            self.ladung = 0.0
            self.reichweite = 0.0
        print('Fahre', gefahren, 'km weit')