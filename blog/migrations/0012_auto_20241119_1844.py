# Generated by Django 2.2.28 on 2024-11-19 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20241119_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipement',
            name='photo',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
