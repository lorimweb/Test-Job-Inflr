from django.db import models


class Config(models.Model):
    name = models.CharField('Nome da Empresa', max_length=150, blank=True)
    slogan = models.CharField('Slogan da Empresa', max_length=255, blank=True)
    phone = models.CharField('Telefone', blank=True, max_length=150)
    address = models.CharField('Endereço', blank=True, max_length=150)
    email = models.CharField('Email', blank=True, max_length=150)
    logo = models.ImageField('Logo Marca', upload_to='logo', blank=True)
    about = models.TextField('Sobre a Empresa', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Configuração'
        verbose_name_plural = 'Configurações'


class SocialNetwork(models.Model):
    config = models.ForeignKey(Config, null=True)
    title = models.CharField('Nome da RedeSocial', max_length=255, blank=True)
    url = models.CharField('Url', max_length=255, blank=True)

    class Meta:
        verbose_name = 'Rede Sociais'
        verbose_name_plural = 'Rede Sociais'
