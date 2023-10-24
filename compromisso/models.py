from django.db import models

class Compromisso(models.Model):
    data = models.DateTimeField()
    descricao = models.TextField()
    local = models.CharField(max_length=50)
    dress_code = models.TextField()
