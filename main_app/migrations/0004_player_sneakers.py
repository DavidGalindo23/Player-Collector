# Generated by Django 2.1.5 on 2019-03-14 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20190313_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='sneakers',
            field=models.ManyToManyField(to='main_app.Sneaker'),
        ),
    ]
