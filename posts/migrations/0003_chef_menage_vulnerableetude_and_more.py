# Generated by Django 4.0.5 on 2022-08-15 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_chef_menage_vulnerablecondi_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='chef_menage',
            name='vulnerableEtude',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='chef_menage',
            name='vulnerableOccup',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='chef_menage',
            name='vulnerableCondi',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='chef_menage',
            name='vulnerablePhy',
            field=models.BooleanField(default=False),
        ),
    ]
