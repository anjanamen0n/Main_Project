# Generated by Django 3.2.20 on 2023-08-06 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SETTINGS', '0008_auto_20230725_1540'),
    ]

    operations = [
        migrations.CreateModel(
            name='Companie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Company', models.CharField(max_length=100)),
                ('Address2', models.CharField(max_length=100)),
                ('Address3', models.CharField(max_length=100)),
                ('Address1', models.CharField(max_length=100)),
                ('Phone', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=100)),
                ('Website', models.CharField(max_length=100)),
                ('Active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Company',
            },
        ),
        migrations.DeleteModel(
            name='Company',
        ),
        migrations.AlterModelOptions(
            name='batch',
            options={'verbose_name_plural': 'Batch'},
        ),
        migrations.AlterModelOptions(
            name='branch',
            options={'verbose_name_plural': 'Branches'},
        ),
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name_plural': 'Course'},
        ),
        migrations.AlterModelOptions(
            name='district',
            options={'verbose_name_plural': 'Districts'},
        ),
        migrations.AlterModelOptions(
            name='enquiry_source',
            options={'verbose_name_plural': 'Enquiry source'},
        ),
        migrations.AlterModelOptions(
            name='follow_up_status',
            options={'verbose_name_plural': 'Follow up status'},
        ),
        migrations.AlterModelOptions(
            name='master_data',
            options={'verbose_name_plural': 'Master Data'},
        ),
        migrations.AlterModelOptions(
            name='qualification',
            options={'verbose_name_plural': 'Qualification'},
        ),
        migrations.AlterModelOptions(
            name='state',
            options={'verbose_name_plural': 'States'},
        ),
        migrations.AlterModelOptions(
            name='syllabus',
            options={'verbose_name_plural': 'Syllabus'},
        ),
        migrations.RenameField(
            model_name='batch',
            old_name='course',
            new_name='Course',
        ),
        migrations.RenameField(
            model_name='branch',
            old_name='District',
            new_name='district',
        ),
        migrations.RemoveField(
            model_name='state',
            name='State',
        ),
        migrations.AddField(
            model_name='enquiry_source',
            name='Active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='qualification',
            name='Active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='state',
            name='state',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='syllabus',
            name='Active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='batch',
            name='End_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='branch',
            name='Branchcode',
            field=models.CharField(max_length=200, verbose_name='Branch Code'),
        ),
    ]
