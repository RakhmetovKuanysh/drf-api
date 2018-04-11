from django.db import models
from django.utils import timezone


class Contact(models.Model):
    """
    Model for Contact
    """
    name = models.CharField(max_length=255, verbose_name=u"Имя")
    surname = models.CharField(max_length=255, verbose_name=u"Фамилия")
    phone_num = models.CharField(max_length=255, 
        verbose_name=u"Номер телефона", unique=True)
    description = models.CharField(max_length=255, verbose_name=u"Описание")
    pub_date = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name + " " + self.surname

    class Meta:
        verbose_name = u'Контакт'
        verbose_name_plural = u'Контакты'
