# Generated by Django 2.2.2 on 2001-01-01 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0008_auto_20010101_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='email',
            field=models.CharField(max_length=100),
        ),
    ]
