# Generated by Django 2.0 on 2018-01-27 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('runtracker', '0003_auto_20180127_0221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='exercisers',
            field=models.ManyToManyField(blank=True, to='runtracker.Exerciser'),
        ),
    ]