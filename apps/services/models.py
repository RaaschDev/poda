from django.db import models
from django.utils.text import slugify
from uuid import uuid4

# Create your models here.
class Service(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255, verbose_name='Nome')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='Slug')
    short_description = models.CharField(max_length=255, verbose_name='Descrição Curta', default='Descrição do serviço')
    description = models.TextField(verbose_name='Descrição')
    image = models.ImageField(upload_to='services/', null=True, blank=True, verbose_name='Imagem')
    initial_page = models.BooleanField(default=True, verbose_name='Página inicial')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'
        ordering = ['-created_at']

class ServiceImage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name='Serviço')
    image = models.ImageField(upload_to='services/', verbose_name='Imagem')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    def __str__(self):
        return self.service.name
    
    class Meta:
        verbose_name = 'Imagem do Serviço'
        verbose_name_plural = 'Imagens dos Serviços'

class ServiceDepoiment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name='Serviço')
    name = models.CharField(max_length=255, verbose_name='Nome')
    description = models.TextField(verbose_name='Descrição')
    note = models.IntegerField(verbose_name='Nota')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    def __str__(self):
        return self.service.name

    class Meta:
        verbose_name = 'Depoimento do Serviço'
        verbose_name_plural = 'Depoimentos dos Serviços'