# Generated by Django 3.2.15 on 2023-11-28 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0009_alter_profile_geslacht'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='thumbnail',
            field=models.CharField(blank=True, max_length=151, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='status',
            field=models.CharField(choices=[('ACTIVE', 'Active'), ('DISABLED', 'Disabled')], default='ACTIVE', max_length=50),
        ),
    ]
