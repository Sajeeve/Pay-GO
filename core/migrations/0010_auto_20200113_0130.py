# Generated by Django 3.0.2 on 2020-01-12 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20200113_0105'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='first_name',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking',
            name='last_name',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
    ]
