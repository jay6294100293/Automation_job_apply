# Generated by Django 5.1.3 on 2024-11-10 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_posts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobposting',
            name='salary',
        ),
        migrations.AddField(
            model_name='jobposting',
            name='salary_currency',
            field=models.CharField(choices=[('USD', 'USD'), ('CAD', 'CAD'), ('EUR', 'EUR'), ('GBP', 'GBP')], default='CAD', max_length=3),
        ),
        migrations.AddField(
            model_name='jobposting',
            name='salary_max',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='jobposting',
            name='salary_min',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected'), ('Interview', 'Interview')], default='Pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='jobposting',
            name='applications_count',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='jobposting',
            name='contract_type',
            field=models.CharField(choices=[('Full-time', 'Full-time'), ('Part-time', 'Part-time'), ('Contract', 'Contract'), ('Temporary', 'Temporary'), ('Internship', 'Internship')], max_length=50),
        ),
        migrations.AlterField(
            model_name='jobposting',
            name='experience_level',
            field=models.CharField(choices=[('Entry level', 'Entry level'), ('Associate', 'Associate'), ('Mid-Senior level', 'Mid-Senior level'), ('Director', 'Director'), ('Executive', 'Executive')], max_length=50),
        ),
    ]