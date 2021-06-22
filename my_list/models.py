from django.db import models

class Bermuda(models.Model):
  message = models.CharField(max_length=200)

