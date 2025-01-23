class doktorats():
    nosaukums = "Nezināms"
    pacSkaits = 0
    def __init__(self, nosaukums = "N/A", pacSkaits = 0):
        self.nosaukums = nosaukums
        self.pacSkaits = pacSkaits
    def ievade(self,):
        self.nosaukums = input("Ievadiet doktorāta nosaukumu: ")
        self.pacSkaits = int(input("Ievadiet pacientu skaitu: "))
    def izvade(self):
        galotne = ""
        if self.pacSkaits%10 != 1:
            galotne = "s"
        print(f"Doktorāts {self.nosaukums} apkalpo {self.pacSkaits} pacientu{galotne}.")    
    
dok1 = doktorats()
dok1.ievade()
dok1.izvade()