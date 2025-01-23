class csddRegistrs():
    def __init__(self, zimols="Nezināms", modelis="Nezināms", registracijasDatums="Nezināms", pilnaMasa="Nezināms", degvielasVeids="Nezināms"):
        self.zimols = zimols
        self.modelis = modelis
        self.registracijasDatums = registracijasDatums
        self.pilnaMasa = pilnaMasa
        self.degvielasVeids = degvielasVeids
    def izvade(self):
        print(f" Zīmols: {self.zimols}\n Modelis: {self.modelis}\n Reģistrācijas datums: {self.registracijasDatums}\n Pilna masa: {self.pilnaMasa}\n Degvielas veids: {self.degvielasVeids}")

auto1= csddRegistrs("Audi", "A4", "22.10.2019", "1800", "BG")
auto1.izvade()            
