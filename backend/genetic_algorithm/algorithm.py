import random
from .models import Individual

class GeneticAlgorithmService:
    def __init__(self, population_size, gene_length):
        self.population_size = population_size
        self.gene_length = gene_length

    def initialize_population(self):
        population = []
        for _ in range(self.population_size):
            individual = Individual(genes=self.generate_random_genes())
            population.append(individual)
        return population

    def calculate_fitness(self, individual):
        genes = individual.genes
        has_albinism = self.check_for_albinism(genes)
        individual.has_albinism = has_albinism

        if has_albinism:
            fitness_score = 0.0
        else:
            fitness_score = 1.0

        return fitness_score

    def check_for_albinism(self, genes):
        # Modify this function to check for albinism based on the specific genetic patterns
        # Return True if the individual has albinism, False otherwise
        return '11' in genes or '00' in genes

    def selection(self, population, num_selected):
        tournament_size = min(5, len(population))
        selected_individuals = []
        for _ in range(num_selected):
            tournament = random.sample(population, tournament_size)
            winner = max(tournament, key=lambda x: self.calculate_fitness(x))
            selected_individuals.append(winner)
        return selected_individuals

    def crossover(self, parent1, parent2):
        crossover_point = random.randint(1, self.gene_length - 1)
        child1_genes = parent1.genes[:crossover_point] + parent2.genes[crossover_point:]
        child2_genes = parent2.genes[:crossover_point] + parent1.genes[crossover_point:]
        child1 = Individual(genes=child1_genes)
        child2 = Individual(genes=child2_genes)
        return child1, child2

    def mutation(self, individual, mutation_rate):
        mutated_genes = ""
        for gene in individual.genes:
            if random.random() < mutation_rate:
                mutated_gene = "1" if gene == "0" else "0"
                mutated_genes += mutated_gene
            else:
                mutated_genes += gene
        individual.genes = mutated_genes

    def evolve_population(self, population, num_selected, mutation_rate):
        new_population = []

        best_individuals = self.selection(population, num_selected)
        new_population.extend(best_individuals)

        while len(new_population) < self.population_size:
            parent1, parent2 = random.sample(best_individuals, 2)
            child1, child2 = self.crossover(parent1, parent2)

            self.mutation(child1, mutation_rate)
            self.mutation(child2, mutation_rate)

            new_population.extend([child1, child2])

        return new_population

    def generate_random_genes(self):
        return "".join(random.choice(["0", "1"]) for _ in range(self.gene_length))
