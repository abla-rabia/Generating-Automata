class Instruction:
    def __init__(self,Si,w,Sj):
        self.Si=Si
        self.w=w
        self.Sj=Sj
    # def __str__(self):
    #     return f"({self.Si}, {self.w}, {self.Sj})"
    def __str__(self):
         return f"Etat: {self.Si.nom}, Symbole: {self.w}, Etat suivant: {self.Sj.nom}"