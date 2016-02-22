from units import Individual

class EvolutionaryAlgorithm():

    def __init__(self):
        # Problem number of problem that is to be solved.
        # 0 OneMax, 1 LOLZ Prefix, 2 Suprising Sequences.
        self.problem_number = 0
        # Solution to the problem.
        self.solution = []
        self.population = []
        # Creates solution for 20-bit OneMax problem.
        for i in range(20):
            self.solution.append(1)
        # Creates first generation of the population.
        for i in range(50):
            self.population.append(Individual())

    # Evaluates the fitness of the whole population.
    def fitness_evaluation(self):
        # Evalutes according to the problems number.
        if self.problem_number == 0:
            # Loops through every individual in the population
            for individual in self.population:
                # Do not calculate the individuals fitness if it has been
                # calculated earlier. Individual may exist for multiple
                # generations.
                if individual.fitness == 0:
                    # Phenotype of current individual.
                    phenotypes = individual.convert_geno_to_pheno()
                    # If the phenotypes is the same as the solution, we do not
                    # need to calculate the fitness. Same as solution length.
                    if phenotypes == self.solution:
                        individual.fitness = len(self.solution)
                    else:
                        for phenotype in phenotypes:
                            if phenotype:
                                individual.fitness += 1

