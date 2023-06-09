from django.db import models


class Post(models.Model):
    title = models.CharField('Заголовок записи', max_length=100)
    description = models.TextField('Текст', null=True)
    author = models.CharField('Автор', max_length=100)
    date = models.DateField('Дата', null=True)

    def __str__(self):
        return f'{self.title}, {self.author}'

    class Meta:
        verbose_name = 'Запис'
        verbose_name_plural = 'Записи'
