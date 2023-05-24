from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Region(models.Model):
    name = models.CharField(
        verbose_name='Viloyat',
        max_length=200
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Viloyat'
        verbose_name_plural = 'Viloyatlar'


class Institution(models.Model):
    name = models.CharField(
        verbose_name='Muassasa',
        max_length=200
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Muassasa'
        verbose_name_plural = 'Muassasalar'


class Status(models.Model):
    name = models.CharField(
        verbose_name='Lavozimi',
        max_length=200
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Lavozim'
        verbose_name_plural = 'Lavozimlar'


class CustomUser(AbstractUser):
    region = models.ForeignKey(
        to=Region,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='users_region'
    )
    institution = models.ForeignKey(
        to=Institution,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='users_institution'
    )
    status = models.ForeignKey(
        to=Status,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='users_status'
    )

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        verbose_name = 'Foydalanuvchi'
        verbose_name_plural = 'Foydalanuvchilar'
