# Generated by Django 3.2.20 on 2023-08-08 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SETTINGS', '0009_auto_20230806_2001'),
    ]

    operations = [
        migrations.AddField(
            model_name='batch',
            name='Batch',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
