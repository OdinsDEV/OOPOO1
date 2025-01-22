class Skolotajs():
    StunduSkaitsNed =0
    skolotajaTips= 0
    uzvards="Nezinams"
class SakumskolasSkolotajs(Skolotajs):
    klase="x.i"
    def __init__(self):
        self.skolotajaTips = 1
    def ievade(self):
        self.uzvards = input("Ievadiet sākumskolas skolotāja uzvārdu: ")
        self.klase = input("Ievadiet sākumskolas skolotāja klasi: ")
        self.StunduSkaitsNed = int(input("Ievadiet sākumskolas skolotāja stundu skaitu nedēļā: "))

    def izvade(self):
        print(f"sākumskolas (tips- {self.skolotajaTips}) skolotājs {self.uzvards} māca {self.StunduSkaitsNed} stundas {self.klase} klasē.")
        exit()

class VidusskolasSkolotajs(Skolotajs):
    def __init__(self):
        self.skolotajaTips =3
    pirmaisPrieksmets= "x priekšmets"
    otraisPrieksmets= "y priekšmets"
    pirmaisPrieksmetsStundas= 0
    otraisPrieksmetsStundas= 0
    def cikStundasKopa(self):
        self.StunduSkaitsNed= self.pirmaisPrieksmetsStundas + self.otraisPrieksmetsStundas
        return self.StunduSkaitsNed
    
    def ievade(self):
        self.uzvards = input("Ievadiet vidusskolas skolotāja uzvārdu: ")
        self.pirmaisPrieksmets = input("Ievadiet pirmo pasniegto priekšmetu: ")
        self.pirmaisPrieksmetsStundas = int(input("Ievadiet pirmā priekšmeta stundas: "))
        self.otraisPrieksmets = input("Ievadiet otro pasniegto priekšmetu: ")
        self.otraisPrieksmetsStundas = int(input("Ievadiet otrā priekšmeta stundas: "))

    def izvade(self):    
        print(f"Vidusskolas (tips - {self.skolotajaTips}) skolotājs {self.uzvards} māca šādus priekšmetus: {self.pirmaisPrieksmets} un {self.otraisPrieksmets}, kopā {self.cikStundasKopa()} stundas.")

#test1 = SakumskolasSkolotajs()
#test1.ievade()
#test1.izvade()



print("Ievadiet skolotāja tipu, kura datus vēlaties ievietot (pamatskola - 1 vidusskola - 3)")
izvele = input("Tips: ")
if izvele == "1":
    test1 = SakumskolasSkolotajs()
    test1.ievade()
    test1.izvade()
if izvele == "3":
    test2 = VidusskolasSkolotajs()
    test2.ievade()
    test2.izvade()
else: 
    print("Ievades kļūda")
    exit()