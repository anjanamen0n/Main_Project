# Generated by Django 3.2.20 on 2023-07-26 06:46

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('SETTINGS', '0008_auto_20230725_1540'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Phone', models.CharField(max_length=30)),
                ('Student', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('Address', models.CharField(max_length=200)),
                ('Dob', models.DateField()),
                ('Street', models.CharField(max_length=50)),
                ('Pincode', models.CharField(max_length=20)),
                ('Gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=50)),
                ('Alternative_email', models.EmailField(max_length=254)),
                ('Alternative_Address', models.CharField(max_length=200)),
                ('Mobile', models.CharField(max_length=30)),
                ('City', models.CharField(max_length=30)),
                ('Whatsapp', models.CharField(max_length=30)),
                ('College_Name', models.CharField(max_length=100)),
                ('Year_of_pass', models.CharField(choices=[('2018', '2018'), ('2019', '2019'), ('2020', '2020'), ('2021', '2021'), ('2022', '2022'), ('2023', '2023')], max_length=50)),
                ('Qualification', models.CharField(choices=[('BE', 'BE'), ('B.Tech', 'B.Tech')], max_length=10)),
                ('Roll_No', models.CharField(max_length=100)),
                ('Registration_No', models.CharField(max_length=100)),
                ('Photo', models.ImageField(upload_to='')),
                ('Student_Call_Status', models.CharField(choices=[('Interested', 'Interested'), ('Not Interesrted', 'Not Interested')], max_length=50)),
                ('Next_Follow_up_Date', models.DateField()),
                ('To_Staff', models.CharField(choices=[('Harsha', 'Harsha'), ('Mini', 'Mini')], max_length=50)),
                ('Comments', models.CharField(max_length=100)),
                ('Course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SETTINGS.course')),
                ('District', smart_selects.db_fields.ChainedForeignKey(chained_field='State', chained_model_field='State', on_delete=django.db.models.deletion.CASCADE, to='SETTINGS.district', verbose_name='District')),
                ('Enquiry_source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SETTINGS.enquiry_source')),
                ('State', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SETTINGS.state')),
            ],
        ),
    ]
