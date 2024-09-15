from django.db import models 

class Form(models.Model):
    username = models.CharField(
        unique=True,
        max_length=30,
        blank=False,
        null=False
    )
    password = models.CharField(
        unique=True,
        max_length=30,
        blank=False,
        null=False
    )

class Posts(models.Model):
    id_p = models.AutoField(primary_key=True)
    title = models.CharField(
        unique=True,
        max_length=30,
        blank=False,
        null=False,
    )
    author = models.CharField(
        unique=False,
        max_length=30,
        blank=False,
        null=False
    )
    text = models.CharField(
        unique=False,
        max_length=900,
        blank=False,
        null=False
    )

    def summary(self):
        # Retorna os primeiros 50 caracteres do texto
        return self.text[:50]
