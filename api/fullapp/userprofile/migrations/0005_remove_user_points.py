# Generated by Django 2.2.6 on 2020-04-02 23:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0004_auto_20200402_2207'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='points',
        ),
    ]
