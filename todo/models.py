from django.db import models
from django.utils import timezone


class Task(models.Model):
    """
    Model for Task
    """
    name = models.CharField(max_length=255)
    pub_date = models.DateTimeField(default=timezone.now)
    done = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'Задание'
        verbose_name_plural = u'Задания'

