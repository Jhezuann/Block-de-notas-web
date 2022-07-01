from django.db import models

class Tareas(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField(blank=True)