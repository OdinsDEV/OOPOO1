class dzivnieks():
    def __init__(self,vards,kajas):
        self.vards=vards
        self.kajas=kajas
    def skanja(self):
        #print("Es esmu ", self.vards, "un man ir", self.kajas, "kājas.")
        print("Random animal noise")
    def __str__(self):
        return f"{self.vards} un {self.kajas} kajas"

class suns(dzivnieks):
    def __init__(self, vards, kajas):
        super().__init__(vards,kajas)
        self.vards="Komisars "+self.vards

class kakis(dzivnieks):
    def __init__(self, vards, kajas):
        print("Mjau!")

d1=dzivnieks("Gauja", 4)
d1.skanja()
k1=kakis("Murris", 4)
s1=suns("Reksis", 4)

print(s1)

