# Generated by Django 3.1.5 on 2021-01-21 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20210121_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issueauthority',
            name='issue_authority_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
