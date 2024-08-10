from django.db import models


class CinemaGeneral(models.Model):
    id_service = models.IntegerField(verbose_name='ID на в МинКульт')
    name = models.CharField(max_length=256, verbose_name='Название кинотеатра')
    description = models.TextField(verbose_name='Описание')
    street = models.CharField(max_length=256, verbose_name='Улица', null=True, blank=True)
    comment = models.TextField(verbose_name='Каментарии', null=True, blank=True)
    full_address = models.CharField(max_length=256, verbose_name='Адрес', null=True, blank=True)
    type = models.CharField(max_length=256, verbose_name='Категория', null=True, blank=True)
    category = models.CharField(max_length=256, verbose_name='Категория', null=True, blank=True)
    category_sysName = models.CharField(max_length=256, verbose_name='SysName', null=True, blank=True)
    website = models.CharField(max_length=256, verbose_name='Сайт', null=True, blank=True)
    email = models.CharField(max_length=256, verbose_name='Email', null=True, blank=True)
    phones = models.CharField(max_length=256, verbose_name='Телефон', null=True, blank=True)

    def __str__(self):
        return self.name
