# Generated by Django 2.0 on 2018-01-27 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('runtracker', '0004_auto_20180127_0222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
