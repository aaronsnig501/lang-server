# Generated by Django 3.0.3 on 2020-07-30 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_auto_20200514_2057'),
    ]

    operations = [
        migrations.AddField(
            model_name='librarybook',
            name='finished_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
