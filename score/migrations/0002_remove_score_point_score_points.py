# Generated by Django 4.0.5 on 2022-06-13 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('score', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='score',
            name='point',
        ),
        migrations.AddField(
            model_name='score',
            name='points',
            field=models.IntegerField(default=0, verbose_name='points'),
            preserve_default=False,
        ),
    ]
