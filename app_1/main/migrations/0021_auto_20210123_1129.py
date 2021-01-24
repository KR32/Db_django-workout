# Generated by Django 3.1.5 on 2021-01-23 11:29

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_auto_20210123_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pqrdetail',
            name='level_id',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='candidate_type_id', chained_model_field='country_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='candidate_level_new', to='main.candidatelevel'),
        ),
        migrations.AlterField(
            model_name='pqrdetail',
            name='qual_country_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='qualification_country_identification', to='main.country_information'),
        ),
        migrations.AlterField(
            model_name='pqrdetail',
            name='qualification_classification_id',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='qual_country_id', chained_model_field='candidate_type_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='qualification_classification_new', to='main.qualificationclassification'),
        ),
    ]
