# Generated by Django 4.1.2 on 2022-10-15 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='employee_Date_of_birth',
            field=models.DateField(blank=True, verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='post',
            field=models.CharField(choices=[('GD', 'Генеральный директор'), ('CA', 'Главный бухгалтер'), ('ED', 'Исполнительный директор')], default='GD', max_length=2, verbose_name='Должность'),
        ),
    ]
