# Generated by Django 4.0.4 on 2022-04-18 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drive', '0002_file_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='share_WHH',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='file',
            name='share_WWS',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='file',
            name='share_WWT',
            field=models.BooleanField(default=False),
        ),
    ]
