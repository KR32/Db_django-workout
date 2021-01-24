# Generated by Django 3.1.5 on 2021-01-22 20:37

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20210122_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pqrheader',
            name='country_authority',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='country_id', chained_model_field='country_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='new_country', to='main.issueauthority'),
        ),
    ]