# Generated by Django 3.0.3 on 2020-04-14 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0004_auto_20200409_2053'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='score',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]