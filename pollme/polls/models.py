from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Poll(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.CharField(max_length = 255)
    pub_date = models.DateField(null = True, blank = True)

    def __str__(self):
        return self.texto        

class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete = models.CASCADE)
    opcao_escolha = models.CharField(max_length = 255)

    def __str__(self):
        return "{} - {}".format(self.poll.texto[:25], self.opcao_escolha[:25])