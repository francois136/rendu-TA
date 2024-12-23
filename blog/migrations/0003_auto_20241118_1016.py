# Generated by Django 2.2.28 on 2024-11-18 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20241118_0925'),
    ]

    operations = [
        migrations.CreateModel(
            name='Personne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='billet',
            name='Personne',
        ),
        migrations.RemoveField(
            model_name='billet',
            name='date',
        ),
        migrations.CreateModel(
            name='Entrainement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_entrainement', models.CharField(choices=[('Natation', 'Natation'), ('Course à pied', 'Course à pied'), ('Cyclisme', 'Cyclisme'), ('Repos', 'Repos')], max_length=20)),
                ('participants', models.ManyToManyField(blank=True, to='blog.Personne')),
            ],
        ),
    ]
