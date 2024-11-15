# Generated by Django 5.1.3 on 2024-11-06 16:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobPosting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=100)),
                ('posted_time', models.CharField(max_length=50)),
                ('published_at', models.DateField()),
                ('job_url', models.URLField()),
                ('company_name', models.CharField(max_length=100)),
                ('company_url', models.URLField()),
                ('description', models.TextField()),
                ('applications_count', models.IntegerField()),
                ('contract_type', models.CharField(max_length=50)),
                ('experience_level', models.CharField(max_length=50)),
                ('work_type', models.CharField(max_length=100)),
                ('sector', models.CharField(max_length=100)),
                ('salary', models.CharField(max_length=50)),
                ('poster_full_name', models.CharField(max_length=100)),
                ('poster_profile_url', models.URLField()),
                ('company_id', models.CharField(max_length=50)),
                ('apply_url', models.URLField()),
                ('apply_type', models.CharField(max_length=50)),
                ('benefits', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applied_on', models.DateField(auto_now_add=True)),
                ('resume', models.FileField(upload_to='resumes/')),
                ('cover_letter', models.FileField(upload_to='cover_letters/')),
                ('status', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='user_profiles.userprofile')),
                ('job_posting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_posts.jobposting')),
            ],
        ),
    ]
