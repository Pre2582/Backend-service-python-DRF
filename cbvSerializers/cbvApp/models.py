from django.db import models

# Create your models here.

class Students(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    department = models.CharField(max_length=100)
    score = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return str(self.id) + " " + self.name + " " + str(self.age) + " " + self.department + " " + str(self.score)
    