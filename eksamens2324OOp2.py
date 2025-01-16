class Skolotajs():
    StunduSkaitsNed =0
    skolotajaTips= 0
    uzvards="Nezinams"
class SakumskolasSkolotajs(Skolotajs):
    klase="x.i"
    def __init__(self):
        self.tips =1
    def izvade(self):
        print(f"sākumskolas (tips- {self.tips}) skolotājs {self.uzvards} māca {skaits} stundas {klase} klasē")

class VidusskolasSkolotajs(Skolotajs):
    def __init__(self):
        self.tips =3
    pirmaisPrieksmets= "x priekšmets"
    otraisPrieksmets= "y priekšmets"
    pirmaisPrieksmetsStundas= 0
    otraisPrieksmetsStundas= 0
    def cikStundasKopa(self):
        self.stunduskaitsned= self.pirmaisPrieksmetsStundas + self.otraisPrieksmetsStundas
    def izvade():    
        print(f"abc")

    