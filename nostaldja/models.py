from django.db import models


class Decade(models.Model):
    start_year = models.CharField(max_length=150)

    def __str__(self):
        return self.start_year


class Fad(models.Model):
    name = models.CharField(max_length=100)
    image_url = models.CharField(max_length=300)
    description = models.TextField(max_length=900)
    decade = models.ForeignKey(Decade, on_delete=models.CASCADE, related_name='fads')

    def __str__(self):
        return self.name
