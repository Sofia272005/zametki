from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Note(models.Model):
    title = models.CharField('Тема заметки', max_length = 30)
    text = models.TextField('Текст заметки')
    date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/{self.id}'