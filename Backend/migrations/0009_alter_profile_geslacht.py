# Generated by Django 3.2.15 on 2023-11-28 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0008_alter_profile_geslacht'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='geslacht',
            field=models.CharField(blank=True, choices=[('MAN', 'Man'), ('ANDERS', 'Anders'), ('VROUW', 'Vrouw')], max_length=50),
        ),
    ]
