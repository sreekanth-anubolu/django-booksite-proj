from django.db import models

# Create your models here.


class Author(models.Model):

    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)


