from django.db import models

# Create your models here.

class WeeklyData(models.Model):
    ErNo = models.CharField(max_length=20)
    advancePython = models.IntegerField(blank=True,default=0,null=True)
    PDC = models.IntegerField()
    SE = models.IntegerField()
    WDD = models.IntegerField(blank=True,default=0,null=True)

    def __str__(self):
        return str(self.ErNo)


class MidData(models.Model):
    ErNo = models.CharField(max_length=20)
    advancePython = models.IntegerField(blank=True,default=0,null=True)
    PDC = models.IntegerField()
    SE = models.IntegerField()
    WDD = models.IntegerField(blank=True,default=0,null=True)

    def __str__(self):
        return str(self.ErNo)


class Student(models.Model):
    Name = models.CharField(max_length=50)
    ErNo = models.CharField(max_length=20)
    BirthDate = models.DateField()

    def __str__(self):
        return str(self.ErNo)

    