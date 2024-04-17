from django.db import models

class Qoshiqchi(models.Model):
    ism = models.CharField(max_length=30)
    tugilgan_yil = models.DateField()
    davlat = models.CharField(max_length=40)

    def __str__(self):
        return self.ism


class Albom(models.Model):
    nom = models.CharField(max_length=300)
    sana = models.DateField()
    rasm = models.FileField(blank=True, null=True)
    qoshiqchi = models.ForeignKey(Qoshiqchi, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom


class Qoshiq(models.Model):
    nom = models.CharField(max_length=30)
    janr = models.CharField(max_length=30)
    davomiylik = models.DurationField(blank=True, null=True)
    fayl = models.FileField(null=True, blank=True)
    albom = models.ForeignKey(Albom, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom




