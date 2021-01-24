# Generated by Django 3.1.5 on 2021-01-22 20:34

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20210122_1725'),
    ]

    operations = [
        migrations.AddField(
            model_name='pqrheader',
            name='country_authority',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='issue_authority_id', chained_model_field='issue_authority_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='new_country', to='main.issueauthority'),
        ),
        migrations.AlterField(
            model_name='issueauthority',
            name='issue_country_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.country_information'),
        ),
    ]