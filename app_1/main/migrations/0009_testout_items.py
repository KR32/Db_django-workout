# Generated by Django 3.1.5 on 2021-01-21 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20210120_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='testout',
            name='items',
            field=models.JSONField(default=None),
        ),
    ]
