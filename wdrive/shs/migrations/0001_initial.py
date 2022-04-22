# Generated by Django 4.0.4 on 2022-04-20 08:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import shs.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(help_text='file အမည်', max_length=255)),
                ('file', models.FileField(upload_to=shs.models.shs_file_path)),
                ('share_MSM', models.BooleanField(default=False)),
                ('share_MDC', models.BooleanField(default=False)),
                ('share_MDN', models.BooleanField(default=False)),
                ('share_MHF', models.BooleanField(default=False)),
                ('share_WWA', models.BooleanField(default=False)),
                ('share_SGS', models.BooleanField(default=False)),
                ('share_SGE', models.BooleanField(default=False)),
                ('share_NWA', models.BooleanField(default=False)),
                ('share_WWM', models.BooleanField(default=False)),
                ('share_AYS', models.BooleanField(default=False)),
                ('share_MGS', models.BooleanField(default=False)),
                ('share_MGN', models.BooleanField(default=False)),
                ('share_MDS', models.BooleanField(default=False)),
                ('share_SHS', models.BooleanField(default=False)),
                ('share_NPT', models.BooleanField(default=False)),
                ('share_YGW', models.BooleanField(default=False)),
                ('share_YGS', models.BooleanField(default=False)),
                ('share_BGW', models.BooleanField(default=False)),
                ('share_YGN', models.BooleanField(default=False)),
                ('share_YGE', models.BooleanField(default=False)),
                ('share_BGE', models.BooleanField(default=False)),
                ('share_MNS', models.BooleanField(default=False)),
                ('share_TNY', models.BooleanField(default=False)),
                ('share_WEC', models.BooleanField(default=False)),
                ('share_WWS', models.BooleanField(default=False)),
                ('share_WWT', models.BooleanField(default=False)),
                ('share_WWH', models.BooleanField(default=False)),
                ('share_WHH', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
