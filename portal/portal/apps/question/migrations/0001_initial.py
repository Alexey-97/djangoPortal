# Generated by Django 4.1.2 on 2022-10-14 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_characteristics', models.CharField(max_length=200, verbose_name='Вопрос характеризуется следующими признаками')),
                ('question', models.CharField(max_length=200, verbose_name='Формулировка вопроса')),
                ('answer', models.TextField(verbose_name='ответ на вопрос')),
                ('topic_answer', models.CharField(choices=[('Fin', 'Финансы'), ('Sel', 'Продажи'), ('Mar', 'Маркетинг')], max_length=3, verbose_name='тема')),
            ],
        ),
    ]
