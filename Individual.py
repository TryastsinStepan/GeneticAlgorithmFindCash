import GlobalParameters
import Chromosome
weight1 = 0
weight2 = 0
weight3 = 0
class Individual:
    def __init__(self, weight1, weight2, weight3):
        self.weight1 = weight1
        self.weight2 = weight2
        self.weight3 = weight3
        self.fitness = self.calculate_fitness()
        chromosome_string = ChromosomeHelper.encode_individual_to_chromosome(self)
        self.chromosome = Chromosome(chromosome_string)

    def calculate_fitness(self):
        fitness = ((self.weight1 / 100) * GlobalParameters.E1) + \
                  ((self.weight2 / 100) * GlobalParameters.E2) + \
                  ((self.weight3 / 100) * GlobalParameters.E3)
        return fitness

    @staticmethod
    def get_best_fitness():
        fitness = ((1 / 100) * GlobalParameters.E1) + \
                  ((1 / 100) * GlobalParameters.E2) + \
                  ((98 / 100) * GlobalParameters.E3)
        return fitness

    def get_chromosome(self):
        return self.chromosome

    def get_weight1(self):
        return self.weight1

    def get_weight2(self):
        return self.weight2

    def get_weight3(self):
        return self.weight3

    def get_fitness(self):
        return self.fitness
