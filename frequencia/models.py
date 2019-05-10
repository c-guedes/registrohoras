from django.db import models

# Create your models here.



class TipoConta(models.Model):
    tipo = models.CharField(max_length=64, verbose_name="Tipo da conta")
    
    def __str__(self):
        return self.tipo

class Funcionario(models.Model):
        usuario = models.CharField(verbose_name="Nome de usuário blog",max_length = 128)
        nome = models.CharField(verbose_name="Nome Completo", max_length = 128)
        senha = models.CharField(verbose_name="Senha",max_length = 128)
        data_de_nascimento = models.CharField(
            'Data de nascimento', blank=True, null=True,max_length = 128)
        tipoConta = models.ForeignKey(TipoConta,on_delete=models.DO_NOTHING,verbose_name="Tipo da conta")

