from django.db import models

class Komanda(models.Model):
    miestas = models.CharField('Miestas', max_length=50)
    pavadinimas = models.CharField('Komandos pavadinimas', max_length=50)
    ikurimo_data = models.IntegerField('Klubas įkurtas')
    saka = models.CharField('Sporto šaka', max_length=50)

    def __str__(self):
        return f'{self.miestas} {self.pavadinimas}'

class Zaidejas(models.Model):
    vardas = models.CharField('Žaidėjo vardas', max_length=50)
    pavarde = models.CharField('Žaidėjo pavardė', max_length=50)
    pozicija = models.CharField('Žaidėjo pozicija', max_length=20)
    amzius = models.IntegerField('Žaidėjo amžius')
    komanda = models.ForeignKey('Komanda', on_delete=models.SET_NULL, null=True, related_name='zaidejas_set')

    def __str__(self):
        return f'{self.vardas} {self.pavarde}'

