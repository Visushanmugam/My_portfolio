from django.db import models

# Create your models here.


class PortfolioContact(models.Model):
    name = models.CharField(max_length=100)
    contactmail = models.CharField(max_length=100)
    message = models.CharField(max_length=5000)




