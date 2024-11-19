# Generated by Django 2.2.28 on 2024-11-18 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20241118_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athlete',
            name='etat',
            field=models.CharField(choices=[('reposé', 'reposé'), ('fatigué', 'fatigué'), ('épuisé', 'épuisé'), ('entrainé', 'entrainé')], max_length=20),
        ),
        migrations.AlterField(
            model_name='equipement',
            name='disponibilite',
            field=models.CharField(choices=[('1', 1), ('2', 2), ('3', 3)], max_length=20),
        ),
    ]