from django.db import models

class Tenhim(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Student(models.Model):
    stName = models.CharField(max_length=50)
    stOvog = models.CharField(max_length=50)
    stcode = models.CharField(max_length=50)
    geriinHayg = models.CharField(max_length=200)
    tursunOgnoo = models.DateTimeField()
    tenhim = models.ForeignKey(Tenhim, on_delete=models.CASCADE)