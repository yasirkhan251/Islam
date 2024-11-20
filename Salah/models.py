from django.db import models
from django.core.validators import MinValueValidator

class Fard_Salah(models.Model):
    salah = models.CharField(max_length=100, unique=True)  # Prayer name
    rakat = models.IntegerField(validators=[MinValueValidator(1)])  # Rakats must be positive
    azan = models.TimeField(blank=True, null=True)  # Azan time, optional
    start_time = models.TimeField()  # Start time
    jamath = models.TimeField()  # Congregation time
    end_time = models.TimeField()  # End time

    def __str__(self):
        return f"{self.salah} ,  ({self.rakat} Rakats), Jamath Time : {self.jamath}"
