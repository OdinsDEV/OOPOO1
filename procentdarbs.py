class turnirs():
    def __init__(self, sportaVeids="Nezināms", cilvekuSkaits="", grupuSkaits="", sponsoruSaraksts = []):
        self.cilvekuSkaits = cilvekuSkaits
        self.grupuskaits = grupuSkaits
        self.sportaVeids = sportaVeids
        self.sponsoruSaraksts = sponsoruSaraksts
    def izvade(self):
        print(f"Šis ir {self.sportaVeids} turnīrs, kurā piedalās {self.cilvekuSkaits} cilvēki, {self.grupuskaits} grupās.")

t1= turnirs("Badmintons", "10", "5")
turnirs.izvade()