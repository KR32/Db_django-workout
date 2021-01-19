# Generated by Django 3.1.5 on 2021-01-19 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_testout_notes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('currency_id', models.IntegerField(primary_key=True, serialize=False)),
                ('country_name', models.CharField(max_length=100, null=True)),
                ('currency_code', models.CharField(max_length=30, null=True)),
                ('currency_name', models.CharField(max_length=100, null=True)),
                ('currency_symbol', models.CharField(max_length=30, null=True)),
                ('comments', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='country_information',
            name='language_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.language'),
        ),
        migrations.AddField(
            model_name='country_information',
            name='currency_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.currency'),
        ),
    ]
