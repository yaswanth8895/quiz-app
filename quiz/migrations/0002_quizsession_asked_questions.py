# Generated by Django 4.2.17 on 2024-12-13 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizsession',
            name='asked_questions',
            field=models.ManyToManyField(related_name='sessions', to='quiz.question'),
        ),
    ]
