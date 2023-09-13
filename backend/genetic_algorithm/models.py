from django.db import models

class Individual(models.Model):
    genes = models.CharField(max_length=255)
    fitness_score = models.FloatField(default=0.0)
    generation = models.IntegerField(default=0)
    has_albinism = models.BooleanField(default=False)


    def __str__(self):
        return self.genes
    
    
    


