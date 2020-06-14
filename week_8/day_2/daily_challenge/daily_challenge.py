class Gene:

    def __init__(self,gene):
        self.gene=gene

    def mutate(self):
        import random
        for x in range(len(self.gene)):
            self.gene[x]=random.randint(0,1)

class Chromosone(Gene):

    def __init__ (self,gene):
        super().__init__(gene)
        self.chromosone=[]
        for i in range(10):
            temp=self.gene.copy()
            self.chromosone.append(temp)

    def mutate(self):
        super().mutate()
        import random
        for v in range(10):
            for x in range(2):
                self.chromosone[v][x]=random.randint(0,1)
            
class DNA(Chromosone):
    def __init__(self,gene):
        super().__init__(gene)
        self.DNA=[]
        for i in range(10):
            temp=self.chromosone.copy()
            self.DNA.append(temp)

    def mutate(self):
        super(Chromosone,self).mutate()
        import random
        for q in range(10):
            for v in range(10):
                for x in range(2):
                    self.DNA[q][v][x]=random.randint(0,1)
    
gene1=Gene([1,0])
gene1.mutate()
print("Gene class",gene1.gene)
print("")


chrom1=Chromosone([1,0])
print("Chromosone class",chrom1.gene)
print(chrom1.chromosone)
print("")

chrom1.mutate()
print("Chromosone mutation",chrom1.chromosone)
print("")

DNA1=DNA([0,1])
print("DNA class",DNA1.gene)
print(DNA1.chromosone)
print(DNA1.DNA)
print("")

DNA1.mutate()
print("DNA mutation",DNA1.DNA)
Organism=DNA([0,1])

num_gens=1

while True:
    temp=[]
    Organism.mutate()
    for q in range(10):
        for v in range(10):
            for x in range(2):
                temp.append(Organism.DNA[q][v][x])
    print(temp)
    if all(element==1 for element in temp):
        break
    print("Generations so far:",num_gens)
    num_gens+=1
    
print("It took {} generations to get all ones in the DNA. That's a probability of {}.".format(num_gens,1/num_gens))
        


