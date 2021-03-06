# Generated by Django 3.1.5 on 2021-01-25 11:39

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_auto_20210125_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qualification',
            name='qualification_level',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='qualification_classification_id', chained_model_field='sort_level', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='qualification_level_new', to='main.qualificationclassification'),
        ),
    ]
