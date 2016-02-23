from random import randint

from bitarray import bitarray


class Individual():

    def __init__(self):
        self.genotypes = bitarray()        
        self.fitness = 0.0
        # Creates random genotypes to individual.
        for i in range(20):
            self.genotypes.extend(str(randint(0,1)))

    # Converts the Individual`s genotypes to phenotypes and returns them.
    def convert_geno_to_pheno(self):
        return bitarray.tolist(self.genotypes)

