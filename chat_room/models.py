from django.db import models
from django.contrib.auth.models import User
# from djoser.urls.base import User


class Room(models.Model):
    """
    Model of room
    """

    name = models.CharField('Наименование', max_length=50, blank=True)
    creator = models.ForeignKey(User, verbose_name="Создатель", on_delete=models.DO_NOTHING)
    invited = models.ManyToManyField(User, verbose_name="Участники", related_name="invited_user", blank=True)
    date = models.DateTimeField("Дата создания", auto_now_add=True, blank=True)
    deleted = models.BooleanField("Удален", default=0)

    class Meta:
        verbose_name = "Комната"
        verbose_name_plural = "Комнаты"


class Message(models.Model):
    """
    Model of chat
    """

    room = models.ForeignKey(Room, verbose_name="Комната", on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    text = models.TextField("Сообщение", max_length=500, blank=True)
    date = models.DateTimeField("Дата отправки", auto_now_add=True, blank=True)
    deleted = models.BooleanField("Удален", default=0)

    class Meta:
        verbose_name = "Сообщение чата"
        verbose_name_plural = "Сообщения чатов"
