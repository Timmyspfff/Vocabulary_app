from django.db import models

class Voc(models.Model):
    vocabulary = models.CharField(max_length=50)
    hant = models.TextField()

    def __str__(self):
        return self.vocabulary
    