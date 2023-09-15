# Generated by Django 3.2.20 on 2023-08-09 09:25

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('SETTINGS', '0010_batch_batch'),
        ('STUDENT', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name_plural': 'Student'},
        ),
        migrations.AddField(
            model_name='student',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Active/Inactive'),
        ),
        migrations.AlterField(
            model_name='student',
            name='Comments',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='Photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '9999999999'. Up to 10 digits allowed.", regex='^\\+?1?\\d{9,10}$')], verbose_name='Phone')),
                ('email', models.EmailField(blank=True, max_length=200, verbose_name='Email')),
                ('batch', models.CharField(max_length=200, verbose_name='Batch')),
                ('have_laptop', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], max_length=100, verbose_name='Do you have laptop')),
                ('isactive', models.BooleanField(default=True, verbose_name='Registered')),
                ('course', models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, to='SETTINGS.course', verbose_name='Course')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='STUDENT.student')),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Trainer')),
            ],
            options={
                'verbose_name_plural': 'Register',
            },
        ),
    ]