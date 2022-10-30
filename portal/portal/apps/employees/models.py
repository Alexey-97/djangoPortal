from django.db import models
import datetime

class Employees(models.Model):
    GD = 'GD'
    CA = 'CA'
    ED = 'ED'
    EMPLOYEE_POST = [
        (GD, 'Генеральный директор'),
        (CA, 'Главный бухгалтер'),
        (ED, 'Исполнительный директор')
    ]
    employee_characteristics = models.TextField('Сотрудник характеризуется')
    employee_full_name = models.CharField('ФИО', max_length=50)
    employee_Date_of_birth = models.DateField('Дата рождения', blank=True, default=datetime.date.today)
    post = models.CharField('Должность', max_length=2, choices=EMPLOYEE_POST, default = GD)
   
    def __str__(self):
        return str(self.post)
    def __str__(self):
        return str(self.employee_full_name)

    class Meta:
        verbose_name_plural = 'Работники'