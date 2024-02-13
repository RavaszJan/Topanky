class Topanka:
    def __init__(self,pohlavie,druh,farba,cena,znacka,velkost):
        self.pohlavie=pohlavie
        self.druh=druh
        self.farba=farba
        self.cena=cena
        self.znacka=znacka
        self.velkost=velkost
        self.is_comleted=False

    def comlete(self):
        self.is_comleted=True


class TopankaModel:
    def __init__(self):
        self.topanky=[]

    def add_topanka(self, topanka):
        self.topanky.appened(topanka)

    def get_topanky(self):
        return self.topanky
