# Generated by Django 3.0.3 on 2020-03-19 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReadingSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.DurationField()),
                ('pages', models.FloatField()),
                ('reading_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.LibraryBooks')),
            ],
        ),
    ]
