# Generated by Django 3.2.15 on 2023-01-01 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0002_alter_profile_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='geslacht',
            field=models.CharField(blank=True, choices=[('MAN', 'Man'), ('VROUW', 'Vrouw'), ('ANDERS', 'Anders')], max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='status',
            field=models.CharField(choices=[('DISABLED', 'Disabled'), ('ACTIVE', 'Active')], default='ACTIVE', max_length=50),
        ),
    ]