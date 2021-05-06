from django.db import models


class HomePageCustomisation(models.Model):
    image = models.ImageField(null=True, blank=True)
