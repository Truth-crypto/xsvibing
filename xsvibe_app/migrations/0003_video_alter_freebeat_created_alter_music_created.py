# Generated by Django 4.2 on 2023-05-26 12:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xsvibe_app', '0002_ads_adsdescription_alter_freebeat_created_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('videoname', models.CharField(max_length=200)),
                ('videotitle', models.CharField(max_length=200)),
                ('video', models.FileField(upload_to='music')),
                ('videoimg', models.ImageField(upload_to='image')),
                ('created', models.TimeField(default=datetime.datetime(2023, 5, 26, 13, 10, 51, 720229))),
            ],
        ),
        migrations.AlterField(
            model_name='freebeat',
            name='created',
            field=models.TimeField(default=datetime.datetime(2023, 5, 26, 13, 10, 51, 720229)),
        ),
        migrations.AlterField(
            model_name='music',
            name='created',
            field=models.TimeField(default=datetime.datetime(2023, 5, 26, 13, 10, 51, 720229)),
        ),
    ]