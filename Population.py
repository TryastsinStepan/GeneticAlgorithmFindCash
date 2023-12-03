import random
import GlobalParameters
from Individual import  *
import ChromosomeHelper

class Population:

    def __init__(self):
        self.individuals = []
        self.random = random
        self.population_size = GlobalParameters.POPULATION_SIZE
        self.maxpoints = {}
        self.avgpoints = {}

    def initialize_population(self):
        for _ in range(self.population_size):
            weight1 = self.get_random_weight()
            weight2 = self.random_weight_in_range(1, 100 - weight1)
            weight3 = 100 - weight1 - weight2
            individual = Individual(weight1, weight2, weight3)
            self.individuals.append(individual)

    def start_simulation(self):
        counter = 0
        generation_number = 1
        prev_best = 0

        prev_avg = 0

        while True:
            print(f"Generation Number: {generation_number}\t")
            new_population = []
            prev_best = max(individual.get_fitness() for individual in self.individuals) or 0
            prev_avg = sum(individual.get_fitness() for individual in self.individuals) / len(self.individuals) or 0
            self.print_info()
            self.maxpoints[generation_number] = max(individual.get_fitness() for individual in self.individuals) or 0
            self.avgpoints[generation_number] =  sum(individual.get_fitness() for individual in self.individuals) / len(self.individuals) or 0
            parent_pool = self.roulette(GlobalParameters.PARENTPOOL_SIZE)

            for i in range(GlobalParameters.PARENTPOOL_SIZE):
                for j in range(GlobalParameters.PARENTPOOL_SIZE):
                    if i != j:
                        new_individual = self.double_crossover(parent_pool[i], parent_pool[j])
                        new_population.append(new_individual)
                if len(new_population) >= self.population_size:
                    break

            self.individuals = new_population
            generation_number += 1

            best_growth = max(individual.get_fitness() for individual in self.individuals) - prev_best
            avg_growth = sum(individual.get_fitness() for individual in self.individuals) / len(
                self.individuals) - prev_avg

            if -0.02 <= best_growth <= 0.02:
                counter += 1
            else:
                counter = 0

            if counter > 10:
                break
            else:
                print("\033[H\033[2J")

        print("Solution found!")
        return generation_number
    def double_crossover(self, parent1, parent2):
        crossover_point1 = self.random.randint(1, 12)
        crossover_point2 = self.random.randint(crossover_point1 + 1, 23)

        parent1_chromosome = parent1.get_chromosome().get_genes()
        parent2_chromosome = parent2.get_chromosome().get_genes()

        child_chromosome = (
            parent1_chromosome[:crossover_point1] +
            parent2_chromosome[crossover_point1:crossover_point2] +
            parent1_chromosome[crossover_point2:]
        )
        child_chromosome = self.mutate_genes(child_chromosome)

        weight1 = ChromosomeHelper.binary_to_decimal(child_chromosome[:8])
        weight2 = ChromosomeHelper.binary_to_decimal(child_chromosome[8:16])
        weight3 = ChromosomeHelper.binary_to_decimal(child_chromosome[16:])

        self.adjust_values(weight1, weight2, weight3)

        return Individual(weight1, weight2, weight3)

    def crossover(self, parent1, parent2):
        crossover_point1 = self.random.randint(1, 23)

        parent1_chromosome = parent1.get_chromosome().get_genes()
        parent2_chromosome = parent2.get_chromosome().get_genes()

        child_chromosome = parent1_chromosome[:crossover_point1] + parent2_chromosome[crossover_point1:]
        child_chromosome = self.mutate_genes(child_chromosome)

        weight1 = ChromosomeHelper.binary_to_decimal(child_chromosome[:8])
        weight2 = ChromosomeHelper.binary_to_decimal(child_chromosome[8:16])
        weight3 = ChromosomeHelper.binary_to_decimal(child_chromosome[16:])

        self.adjust_values(weight1, weight2, weight3)

        return Individual(weight1, weight2, weight3)

    def adjust_values(self, value1, value2, value3):
        total_sum = value1 + value2 + value3
        value1 = (value1 * 100) // total_sum
        value2 = (value2 * 100) // total_sum
        value3 = (value3 * 100) // total_sum
        difference = 100 - (value1 + value2 + value3)

        if value1 == 0 or value2 == 0 or value3 == 0:
            max_value = max(value1, max(value2, value3))
            if value1 == 0:
                value1 += 1
            elif value2 == 0:
                value2 += 1
            elif value3 == 0:
                value3 += 1

            if max_value == value1:
                value1 -= 1
            elif max_value == value2:
                value2 -= 1
            else:
                value3 -= 1

    def mutate_genes(self, genes):
        chromosome = list(genes)
        for i in range(len(chromosome)):
            if self.random.randint(1, 100) == 1:
                chromosome[i] = '1' if chromosome[i] == '0' else '0'
        return ''.join(chromosome)

    def get_random_weight(self):
        return self.random.randint(1, 97)

    def random_weight_in_range(self, min_val, max_val):
        return self.random.randint(min_val, max_val)

    def roulette(self, pull_size):
        popul = list(self.individuals)
        pull = []

        individuals_for_selection = popul[:]

        individuals_for_selection.sort(key=lambda x: x.get_fitness(), reverse=True)

        sum_fitness = sum(individual.get_fitness() for individual in individuals_for_selection)

        probability = [individual.get_fitness() / sum_fitness for individual in individuals_for_selection]

        for _ in range(pull_size):
            tik = self.random.uniform(0, 1)
            a = 0
            for j in range(len(probability)):
                a += probability[j]
                if a > tik:
                    pull.append(individuals_for_selection[j])
                    break

        return pull

    def roulette_wheel_selection(self, probabilities):
        random_value = self.random.uniform(0, 1)
        cumulative_probability = 0

        for i in range(len(probabilities)):
            cumulative_probability += probabilities[i]
            if random_value <= cumulative_probability:
                return i

        return len(probabilities) - 1

    def get_ratios(self, individuals):
        total_fitness = sum(individual.get_fitness() for individual in individuals)
        ratios = [individual.get_fitness() / total_fitness for individual in individuals]
        return ratios

    def print_info(self):
        avg_fitness = sum(individual.get_fitness() for individual in self.individuals) / len(self.individuals)
        max_fitness = max(individual.get_fitness() for individual in self.individuals)

        print(f"Средняя fitness: {avg_fitness}")
        print(f"Лучшая fitness: {max_fitness}")
    def get_avgpoints(self):
        return self.avgpoints
    def get_maxpoints(self):
        return self.maxpoints

