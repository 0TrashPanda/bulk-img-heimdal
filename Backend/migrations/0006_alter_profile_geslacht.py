# Generated by Django 3.2.15 on 2023-11-27 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0005_auto_20230211_0232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='geslacht',
            field=models.CharField(blank=True, choices=[('MAN', 'Man'), ('VROUW', 'Vrouw'), ('ANDERS', 'Anders')], max_length=50),
        ),
    ]
