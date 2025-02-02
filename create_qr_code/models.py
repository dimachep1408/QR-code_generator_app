from django.db import models
from django.contrib.auth.models import User
import datetime


# Create your models here.
class QrCodes(models.Model):
    name = models.CharField(max_length= 20, unique= False)
    image = models.TextField(default= "none")
    user = models.ForeignKey(User, models.CASCADE)
    date = models.DateField(default= datetime.date.today())