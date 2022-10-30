# from pyexpat import model
# from random import choices
from multiprocessing import Value
from django.db import models


class Question(models.Model):
    Fin = 'Fin'
    Sal = 'Sel'
    Mar = 'Mar'
    TOPIC_ANSWER = [
        (Fin, 'Финансы'),
        (Sal, 'Продажи'),
        (Mar, 'Маркетинг')
    ]

    question_characteristics = models.CharField('Вопрос характеризуется следующими признаками',max_length=200)
    question = models.CharField('Формулировка вопроса',max_length=200)
    answer = models.TextField('Ответ на вопрос')
    topic_answer = models.CharField('Тема', max_length=10, choices=TOPIC_ANSWER)



    def __str__(self):
        return self.question

    class Meta:
        verbose_name_plural = 'Вопросы'

    