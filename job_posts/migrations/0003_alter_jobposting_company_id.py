# Generated by Django 5.1.3 on 2024-11-13 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_posts', '0002_remove_jobposting_salary_jobposting_salary_currency_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobposting',
            name='company_id',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
