from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from musicians.models import Musician
# Create your models here.


class Album(models.Model):
    name = models.CharField(max_length=60)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    release = models.DateField()
    CHOICES = [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')]
    # ratings= models.Mul
    # ratins = models.CharField(max_length=5, validators=[max(5), min(1)])
    rating = models.PositiveIntegerField(
        default=0,
        validators=[MinValueValidator(
            limit_value=1), MaxValueValidator(limit_value=5)]
    )

    def __str__(self):
        return self.name
