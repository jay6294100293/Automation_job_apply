# Generated by Django 5.1.3 on 2024-11-08 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Responsibility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='experience',
            name='responsibilities',
        ),
        migrations.AddField(
            model_name='experience',
            name='responsibilities',
            field=models.ManyToManyField(blank=True, to='user_profiles.responsibility'),
        ),
    ]
