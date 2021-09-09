from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import AutoField

from authors.models import Author
# Create your models here.


class Books(models.Model):
    title = models.CharField(max_length=80)
    author = models.ForeignKey(Author, on_delete=CASCADE)
    stock = models.SmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    desc = models.TextField()



