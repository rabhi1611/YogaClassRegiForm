from django.db import models


# Create your models here.
class Month(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Batch(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField(default="gmail.com")
    age = models.IntegerField()

    Month = models.ForeignKey(Month, on_delete=models.CASCADE)

    Batch = models.ForeignKey(Batch, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
