from modules.instruction import Instruction


class Automate:
    def __init__(self,X):
        self.X=X

    def constAutoTrivial(self,expR):
        if (expR=="EV"):#ensemble vide
            self.S0 = Etat()
            self.F = [Etat()]
            self.S=[self.S0]+self.F
            self.I=None
        elif (expR=="motVide"):
            self.S0=Etat()
            self.F=[self.S0]
            self.S=[self.S0]
            self.I=None
        else:
            self.S0=Etat()
            self.F=[Etat()]
            self.S=[self.S0]+self.F
            self.I=[Instruction(self.S[0],expR,self.S[1])]
    def constAutomate(self,exp):
        if len(exp.ER)<=1:
            self.constAutoTrivial(exp.ER)
        # else:
        #     ER.extractionOp()
    

    def Union(self,B):#self et B deux automates
        S0=Etat()
        self.S+=[S0]
        self.I+=B.I
        self.I+=[Instruction(S0,"motVide",self.S0)]
        self.I+=[Instruction(S0,"motVide",B.S0)]
        self.S0=S0
        self.F+=B.F
        self.S+=B.S
      
       
    def ConcatenationDroite(self,B): #notre automate ensute B ie self.B
        self.S+=B.S
        for i in self.F : 
            self.I+=[Instruction(i,"motVide",B.S0)]
        self.F=B.F
        self.I+=B.I
    def ConcatenationGauche(self,B):#B.self
        self.S+=B.S
        for i in B.F : 
            self.I+=[(Instruction(i,"motVide",self.S0))]
        self.S0=B.S0
        self.I+=B.I
        
    def Iteration(self):
        S0=Etat()
        Sf=Etat()
        self.S+=[S0]
        self.S+=[Sf]
        self.I+=[Instruction(S0,"motVide",self.S0)]
        for i in self.F : 
            self.I+=[Instruction(i,"motVide",Sf)]
        self.S0=S0
        self.F=[S0,Sf]
        self.I+=[Instruction(Sf,"motVide",S0)]
    def printAutomate(self):
        print("Ensemble",f"{self.X}")
        print("Etat intiale",f"{self.S0}")
        for s in self.S:
            print("Etats",f"{s}")
        for sf in self.F:    
            print("Etat Finaux",f"{sf}")
        for i in self.I:  
            print("Instruction",f"{i}")  
        
        
class Etat:
    cpt_etat=0
    def __init__(self):
        self.nom="S"+str(Etat.cpt_etat)
        Etat.cpt_etat=Etat.cpt_etat+1
    def __str__(self):
        return f"{self.nom}"
      