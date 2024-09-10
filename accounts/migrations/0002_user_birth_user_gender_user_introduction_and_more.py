# Generated by Django 4.2 on 2024-09-10 05:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birth',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, choices=[('m', '남성'), ('f', '여성')], max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='introduction',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='user',
            name='nickname',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
