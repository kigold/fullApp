# Generated by Django 3.0.5 on 2020-04-18 21:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0005_auto_20200415_2236'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='challenge',
            options={'ordering': ['-pk']},
        ),
    ]
