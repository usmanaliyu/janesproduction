# Generated by Django 2.2 on 2020-07-05 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200701_2023'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='phone',
            field=models.CharField(max_length=20, null=True),
        ),
    ]