# Future Reference:
# Put these "Blocks" in a seperate app next time
from django.db import models



class HomePageCustomisation(models.Model):
    home_page_title = models.CharField(null=True, blank=True, max_length=120)
    image = models.ImageField(null=True, blank=True)
    
    class Meta:
        verbose_name = "Home Page"


class NavbarCustomisation(models.Model):
    link_1 = models.CharField(null=False, blank=False, max_length=25)
    link_2 = models.CharField(null=False, blank=False, max_length=25)
    link_3 = models.CharField(null=False, blank=False, max_length=25)
    link_4 = models.CharField(null=False, blank=False, max_length=25)

    class META:
        verbose_name = 'Navbar'
