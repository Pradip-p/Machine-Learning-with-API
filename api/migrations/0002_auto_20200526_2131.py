# Generated by Django 2.1.5 on 2020-05-27 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='titanic',
            name='Pclass',
            field=models.IntegerField(default=0),
        ),
    ]
