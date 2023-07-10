# Generated by Django 4.2.2 on 2023-07-09 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_uploadmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='imageUrl',
        ),
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(default='', upload_to='images'),
        ),
    ]