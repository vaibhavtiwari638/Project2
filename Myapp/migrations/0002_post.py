# Generated by Django 4.1 on 2024-01-20 06:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('uname', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=60)),
                ('image', models.ImageField(upload_to='blog_images/')),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=60)),
                ('slug', models.CharField(max_length=130)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]