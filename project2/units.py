from random import randint

from bitarray import bitarray


class Individual():

    def __init__(self):
        self.genotype = bitarray()        
        self.fitness = 0.0
        # Creates random genotype to individual.
        for i in range(20):
            self.genotype.extend(str(randint(0,1)))

    # Converts the Individual`s genotype to phenotype and returns them.
    def convert_geno_to_pheno(self):
        return bitarray.tolist(self.genotype)

