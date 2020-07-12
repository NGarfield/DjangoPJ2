from django.db import models

# Create your models here.

class Profile(models.Model):
    id = models.CharField(max_length=10,unique=True,primary_key=True)
    name = models.CharField(max_length=250,unique=True)
    faculty = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    calculatedCredits = models.IntegerField()
    registeredCredits = models.IntegerField()
    creditsAchieved = models.IntegerField()
    gradeAverage = models.FloatField()

    def __str__(self):
        return str(self.id)+" "+self.name

class RegisteredSubject(models.Model):
    idSubject = models.CharField(max_length=6,primary_key=True)
    nameSubject = models.CharField(max_length=255)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    grade = models.CharField(max_length=2)

    def __str__(self):
        return str(self.profile)+" "+str(self.idSubject)+" "+self.nameSubject

    



