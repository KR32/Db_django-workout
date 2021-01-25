# Generated by Django 3.1.5 on 2021-01-25 11:50

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_auto_20210125_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qualification',
            name='qualification_level',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='qualification_classification_id', chained_model_field='qualification_classification_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='qualification_level_new', to='main.qualificationclassification'),
        ),
    ]
