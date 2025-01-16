class doktorats():
    def __init__(self, nosaukums="N/A", skaits=0):
        self.skaits = skaits
    def ievade(self):
        self.nosaukums= input("Ievadiet nosaukumu: ")
        self.skaits = int(input("Ievadiet pacientu skaitu: "))

    def izvade(self):
        galotne=""
        if (self.skaits%10 !=1):
            galotne="s"
        print(f"Doktorāts {self.nosaukums} apkalpo {self.skaits} pacientu{galotne}.")    

d1= doktorats("slimnica", 21)
d1.ievade()
d1.izvade()