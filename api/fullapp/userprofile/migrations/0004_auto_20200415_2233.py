# Generated by Django 3.0.5 on 2020-04-15 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0003_auto_20200413_1128'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cupgame',
            options={'ordering': ['-pk']},
        ),
        migrations.AlterModelOptions(
            name='leaguegame',
            options={'ordering': ['-pk']},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['pk']},
        ),
        migrations.AlterModelOptions(
            name='team',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='league',
            name='is_two_leg',
            field=models.BooleanField(default=True, null=True),
        ),
    ]
