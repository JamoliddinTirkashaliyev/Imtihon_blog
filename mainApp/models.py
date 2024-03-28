from django.contrib.auth.models import User
from django.db import models



class Muallif(models.Model):
    ism = models.CharField(max_length=250,  blank=True,null=True)
    yosh = models.PositiveIntegerField( blank=True,null=True)
    kasb = models.CharField(max_length=250, blank=True,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.ism


class Maqola(models.Model):
    sarlavha = models.CharField(max_length=250)
    sana = models.DateField()
    mavzu = models.TextField()
    matn = models.TextField()
    muallif = models.ForeignKey(Muallif,on_delete=models.CASCADE)
