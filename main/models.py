from django.db import models


# Create your models here.

class EqualityCondition(models.Model):
    firstCondition = models.TextField()
    secondCondition = models.TextField()
