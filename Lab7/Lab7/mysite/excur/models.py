from django.db import models

# Create your models here.

class Client(models.Model):
    surname = models.TextField(verbose_name='Фамилия')
    name = models.TextField(verbose_name='Имя')
    phone = models.TextField(verbose_name='Телефон')

    def __unicode__(self):
        return self.surname

    def __str__(self):
        return self.surname

class Destination(models.Model):
    region = models.TextField(verbose_name='Регион')
    country = models.TextField(verbose_name='Страна')
    place_name = models.TextField(verbose_name='Название места')

    def __unicode__(self):
        return self.place_name

    def __str__(self):
        return self.place_name

class Guide(models.Model):
    surname = models.TextField(verbose_name='Фамилия')
    name = models.TextField(verbose_name='Имя')
    phone = models.TextField(verbose_name='Телефон')

    def __unicode__(self):
        return self.surname

    def __str__(self):
        return self.surname

class Excursion_template(models.Model):
    id_destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    id_guide = models.ForeignKey(Guide, on_delete=models.CASCADE)

class Excursion_client(models.Model):
    id_template = models.ForeignKey(Excursion_template, on_delete=models.CASCADE)
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)
