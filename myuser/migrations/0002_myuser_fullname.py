# Generated by Django 3.2.16 on 2022-11-07 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myuser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='fullname',
            field=models.CharField(default='', max_length=100),
        ),
    ]
