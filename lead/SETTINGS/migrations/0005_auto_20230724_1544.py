# Generated by Django 3.2.20 on 2023-07-24 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SETTINGS', '0004_rename_state_branch_state'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='state',
            options={},
        ),
        migrations.AddField(
            model_name='state',
            name='Active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='state',
            name='State',
            field=models.CharField(max_length=250),
        ),
    ]
