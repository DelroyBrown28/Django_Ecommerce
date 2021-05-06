from django.db import models


class HomePageCustomisation(models.Model):
    home_page_title = models.CharField(null=True, blank=True, max_length=120)
    image = models.ImageField(null=True, blank=True)
