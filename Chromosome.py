class Chromosome:
    def __init__(self,genes):
        self.genes = genes
    def get_genes(self):
        return self.genes
    def set_genes(self,genes:str):
        self.genes = genes
    def print_chromosome(self):
        print("This is chromosome")


