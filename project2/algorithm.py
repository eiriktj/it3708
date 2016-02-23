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
        # Statistics
        self.generation_number = 0
        self.best_fitness = 0.0
        self.average_fitness = 0.0
        self.standard_deviation = 0.0
        self.best_phenotype = []
        # False when solution is found
        self.no_solution = True
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
        # List of fitness of the population
        self.population_fitness = []
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
        # Starting loop
        self.evolutionary_loop()

    def evolutionary_loop(self):
        self.children = self.population
        self.fitness_evaluation()
        self.logging_routine()
        while self.no_solution:
            print('Loop')
            self.mate_selection()
            self.adult_selection()

            self.no_solution = False

        print('Population genotypes: ')
        for individual in self.population:
            print(individual.genotype)
        print(' Population fitness: ' + str(self.population_fitness))

    # Evaluates the fitness of the whole population.
    def fitness_evaluation(self):
        # Evalutes according to the problems number.
        if self.problem_number == 0:
            self.one_max()

    def one_max(self):
        # Loops through every new individual.
        for index, individual in enumerate(self.children):
                # Phenotype of current individual.
                phenotype = individual.convert_geno_to_pheno()
                # If the phenotype is the same as the solution, we do not
                # need to calculate the fitness. Same as the highest fitness
                # value 1.
                if phenotype == self.solution:
                    self.children[index].fitness = 1.0
                    self.no_solution = False
                else:
                    # Calculates error E_j.
                    for pheno in phenotype:
                        if pheno == 0:
                            individual.fitness += 1.0
                    # Calculates fitness F_j.
                    self.children[index].fitness = 1.0/(1.0+individual.fitness)

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
            return self.sigma_scaling()


    #def fitness_proportionate(self):

    def sigma_scaling(self):
        # List of the fitness values of the population.
        population_fitness = []
        for individual in self.population:
            population_fitness.append(individual.fitness)
        # 2 times the standard deviation of the fitness.
        standard_deviation_2 = 2*np.std(population_fitness)
        # The mean of the populations fitness.
        mean = np.mean(population_fitness)
        # Sigma scaled fitness of the population.
        sigma_fitness = []
        for fitness in population_fitness:
            sigma_fitness.append(1+((fitness-mean)/standard_deviation_2))
        return sigma_fitness

    #def tournament_selection(self):

    #def unknown_mechanism(self):

    def mutation(self, genotypes):
        if self.problem_number == 0:
            #Creates genotype for new individual.
            new_genotype = bitarray()
            for geno in genotype:
                if random() <= self.mutation_rate:
                    new_genotype.extend(str(randint(0,1)))
                else:
                    new_genotype.extend(str(int(geno)))
        return new_genotype

    def crossover(self, genotype1, genotype2):
        new_genotype = bitarray()
        for i in range(len(genotype1)):
            if random() <= self.crossover_rate:
                new_genotype.extend(str(int(genotype1[i])))
            else:
                new_genotype.extend(str(int(genotype2[i])))
        return new_genotype

    # Calculates and logs statistics.
    def logging_routine(self):
        self.population_fitness = []
        for individual in self.population:
            self.population_fitness.append(individual.fitness)
        self.generation_number += 1
        self.average_fitness = np.mean(self.population_fitness)
        self.standard_deviation = np.std(self.population_fitness)
        # Index of individual with best fitness.
        best_index = np.argmax(self.population_fitness)
        self.best_fitness = self.population_fitness[best_index]
        self.best_phenotype = self.population[best_index].convert_geno_to_pheno()
        print('Generation Number: ' + str(self.generation_number))
        print('Average Fitness: ' + str(self.average_fitness))
        print('Standard Deviation: ' + str(self.standard_deviation))
        print('Best Fitness: ' + str(self.best_fitness))
        print('Best Phenotype: ' + str(self.best_phenotype))

    #def plotting routine(self):

