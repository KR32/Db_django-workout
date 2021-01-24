# Generated by Django 3.1.5 on 2021-01-23 15:49

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_auto_20210123_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='country',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='continent', chained_model_field='continent', on_delete=django.db.models.deletion.CASCADE, show_all=True, to='main.country'),
        ),
        migrations.AlterField(
            model_name='pqrdetail',
            name='issue_authority_id',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='qualification_id', chained_model_field='issue_country_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='issue_authority_new', show_all=True, to='main.issueauthority'),
        ),
        migrations.AlterField(
            model_name='pqrdetail',
            name='level_id',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='candidate_type_id', chained_model_field='country_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='candidate_level_new', show_all=True, to='main.candidatelevel'),
        ),
        migrations.AlterField(
            model_name='pqrdetail',
            name='qualification_classification_id',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='qual_country_id', chained_model_field='candidate_type_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='qualification_classification_new', show_all=True, to='main.qualificationclassification'),
        ),
        migrations.AlterField(
            model_name='pqrdetail',
            name='qualification_id',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='qualification_classification_id', chained_model_field='qualification_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='qualification_new', show_all=True, to='main.qualification'),
        ),
    ]
