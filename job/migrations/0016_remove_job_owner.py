# Generated by Django 4.1.6 on 2023-02-13 00:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0015_rename_user_job_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='owner',
        ),
    ]
