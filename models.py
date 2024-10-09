from email.mime import image
from operator import truediv
from pickle import TRUE
from uuid import uuid4
import uuid
from django.db import models


class blogTable(models.Model):
    name = models.CharField(max_length=200)
    discription = models.TextField(null = True, blank= True)
    image = models.ImageField(default='static/images/images1.jpeg', null = True, blank = True)
    image1 = models.ImageField(default='static/images/images1.jpeg', null = True, blank = True)
    image2 = models.ImageField(default='static/images/images1.jpeg', null = True, blank = True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)

    def __str__(self) :
        return self.name

# Create your models here.
