# Generated by Django 2.2.2 on 2020-06-06 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attachment',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
