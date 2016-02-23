from random import random
from random import randint

from bitarray import bitarray
import numpy as np

from units import Individual

class EvolutionaryAlgorithm():

    def __init__(self):
        # Problem number of problem that is to be solved.
        # 0 OneMax, 1 LOLZ Prefix, 2 Suprising Sequences.
        self.problem_number = 0
        # Type of adult selection protocol.
        # 0 full, 1 over-production, 2 mixing.
        self.selection_protocol = 2
        # Type of mechanism for mate selection.
        # 0 fitness+proportionate, 1 sigma-scaling, 2 tournament selection, 3
        # unknown_mechanism
        self.selection_mechanism = 1
        # Generation number.
        self.generation_number = 0
        # Number of survivors from previous generation.
        self.adult_survivors = 5
        # How much recombination that is done between two individuals in a
        # crossover.
        self.crossover_rate = 0.5
        #How much of the genes that are mutated
        self.mutation_rate = 0.05
        # Solution to the problem.
        self.solution = []
        # Adult population.
        self.population = []
        # Children of the new generation.
        self.children = []
        # Individuals from previous generation
        self.master_race = []
        # Creates solution for 20-bit OneMax problem.
        for i in range(20):
            self.solution.append(1)
        # Creates first generation of the population.
        for i in range(50):
            self.population.append(Individual())
        # Number of individuals in the new generation.
        self.number_of_individuals = len(self.population)

    # Evaluates the fitness of the whole population.
    def fitness_evaluation(self):
        # Evalutes according to the problems number.
        if self.problem_number == 0:
            self.one_max()

    def one_max(self):
        # Loops through every new individual.
        for individual in self.children:
                # Phenotype of current individual.
                phenotypes = individual.convert_geno_to_pheno()
                # If the phenotypes is the same as the solution, we do not
                # need to calculate the fitness. Same as the highest fitness
                # value 1.
                if phenotypes == self.solution:
                    individual.fitness = 1.0
                else:
                    # Calculates error E_j.
                    for phenotype in phenotypes:
                        if phenotype == 0:
                            individual.fitness += 1.0
                    # Calculates fitness F_j.
                    individual.fitness = 1.0/(1.0+individual.fitness)

    #def lolz_prefix(self):

    #def suprising_sequences(self):

    def adult_selection(self):
        if self.selection_protocol == 2:
            self.generational_mixing()

    #def full_replacement(self):

    #def over_production(self):

    def generational_mixing(self):
        # List of individuals from the generation.
        previous_generation = self.population
        self.master_race = []
        for i in range(self.adult_survivors):
            # Index of fittest individual in remaining individuals in previous
            # generation.
            fittest_index = np.argmax(previous_generation)
            # Adds currently fittest individual from the previous generation to
            # the next and removes it from the previous.
            self.master_race.append(previous_generation.pop(fittest_index))

    def mate_selection(self):
        if self.selection_mechanism == 1:
            self.sigma_scaling

    #def fitness_proportionate(self):

    #def sigma_scaling(self):

    #def tournament_selection(self):

    #def unknown_mechanism(self):

    def mutation(self, genotypes):
        if self.problem_number == 0:
            #Creates genotypes for new individual.
            new_genotypes = bitarray()
            for genotype in genotypes:
                if random() <= self.mutation_rate:
                    new_genotypes.extend(str(randint(0,1)))
                else:
                    new_genotypes.extend(str(int(genotype)))
        return new_genotypes

    def crossover(self, genotypes1, genotypes2):
        new_genotypes = bitarray()
        for i in range(len(genotypes1)):
            if random() <= self.crossover_rate:
                new_genotypes.extend(str(int(genotypes1[i])))
            else:
                new_genotypes.extend(str(int(genotypes2[i])))
        return new_genotypes

    #def evolutionary_loop(self):

    #def logging_routine(self):

    #def plotting routine(self):

