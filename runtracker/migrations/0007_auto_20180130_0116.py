# Generated by Django 2.0 on 2018-01-30 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('runtracker', '0006_auto_20180130_0107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='media/activities'),
        ),
    ]
