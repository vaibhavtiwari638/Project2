# Generated by Django 4.1 on 2024-01-20 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0003_patientprofile_rename_userprofile_doctorprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientprofile',
            name='address',
            field=models.CharField(default='', max_length=100),
        ),
    ]
