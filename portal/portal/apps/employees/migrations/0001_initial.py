# Generated by Django 4.1.2 on 2022-10-14 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_characteristics', models.TextField(verbose_name='Сотрудник характеризуется')),
                ('employee_full_name', models.CharField(max_length=50, verbose_name='ФИО')),
                ('employee_Date_of_birth', models.DateField(auto_now_add=True, verbose_name='Дата рождения')),
                ('post', models.CharField(choices=[('GD', 'Генеральный директор'), ('CA', 'Главный бухгалтер'), ('ED', 'Исполнительный директор')], max_length=2, verbose_name='Должность')),
            ],
        ),
    ]
