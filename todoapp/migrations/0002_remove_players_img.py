# Generated by Django 4.2.1 on 2023-07-04 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='players',
            name='img',
        ),
    ]