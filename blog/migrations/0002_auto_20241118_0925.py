# Generated by Django 2.2.28 on 2024-11-18 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='billet',
            old_name='descrition',
            new_name='description',
        ),
    ]
