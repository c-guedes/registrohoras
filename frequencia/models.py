from django.db import models

# Create your models here.


class Funcionario(models.Model):
        usuario = models.CharField(verbose_name="Nome de usuário blog",max_length = 128)
        nome = models.CharField(verbose_name="Nome Completo", max_length = 128)
        senha = models.CharField(verbose_name="Senha",max_length = 128)
        data_de_nascimento = models.CharField(
            'Data de nascimento', blank=True, null=True,max_length = 128)
        chefe = models.ForeignKey("Funcionario",blank=True, null=True,verbose_name="AAA", on_delete=models.CASCADE)