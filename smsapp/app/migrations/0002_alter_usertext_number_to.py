# Generated by Django 4.0 on 2021-12-20 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertext',
            name='number_to',
            field=models.CharField(max_length=11),
        ),
    ]
