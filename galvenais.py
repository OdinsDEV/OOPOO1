from abc import ABC, abstractmethod

class dzivnieks(ABC): #Parent class
    def __init__(self,vards,kajas):
        self.vards=vards
        self.kajas=kajas

    @abstractmethod    #parāda ka nākamā metode būs abstrakta    
    def skanja(self):
        print("Random animal noise")
    def __str__(self):
        return f"{self.vards} un {self.kajas} kajas"

class suns(dzivnieks): #Child class
    def __init__(self, vards, kajas):
        super().__init__(vards,kajas)
        self.vards="Komisars "+self.vards
    def skanja(self):
        print("Wof wof!")

class kakis(dzivnieks): #Child class
    def __init__(self, vards, kajas):
        super().__init__(vards,kajas)
        self.vards="Kaķītis "+self.vards
    def skanja(self):
        print("Mjau Mjau!")

class govs(dzivnieks):
    def skanja(self):
        print("Muuuuuuuu!")

listDzivnieki = []       #izveidots dzivnieku saraksts 

listDzivnieki.append(suns("volvis", 4)) #sarakstam pievieno dzivnieku
listDzivnieki.append(suns("Bella", 4))
listDzivnieki.append(suns("Dalmacietis", 4))
listDzivnieki.append(suns("Žiglais", 4))


listDzivnieki.append(kakis("Pichuks", 4))
listDzivnieki.append(kakis("Rozine", 4))
listDzivnieki.append(kakis("Rizhais", 4))

listDzivnieki.append(govs("Gauja", 4))
listDzivnieki.append(govs("Venta", 4))

for dzivnieks in listDzivnieki: #Izprintē katru dzīvnieku 
    print(dzivnieks)
    dzivnieks.skanja()

#d1=dzivnieks("Gauja", 4)
# d1.skanja()
# k1=kakis("Murris", 4)
# s1=suns("Reksis", 4)

#print(s1)

