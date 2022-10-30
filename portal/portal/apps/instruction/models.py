from tabnanny import verbose
from django.db import models
from employees.models import Employees


class Instructions(models.Model):
    technical_requirements = models.TextField('Инструкция характеризуется следующими признаками')
    topic = models.CharField('Тема', max_length=100)
    author = models.ForeignKey(Employees, on_delete=models.CASCADE, verbose_name='Автор')
    date = models.DateField('Дата', auto_now_add=True)
    file_link = models.URLField('Ссылка на файл')

    def __str__(self):
        return str(self.topic)

    class Meta:
        verbose_name_plural = 'Инструкции'
