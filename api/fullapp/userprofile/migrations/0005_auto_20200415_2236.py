# Generated by Django 3.0.5 on 2020-04-15 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0004_auto_20200415_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='league',
            name='is_two_leg',
            field=models.BooleanField(default=True),
        ),
    ]
