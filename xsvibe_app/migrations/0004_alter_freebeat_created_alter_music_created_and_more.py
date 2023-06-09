# Generated by Django 4.2 on 2023-05-27 08:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xsvibe_app', '0003_video_alter_freebeat_created_alter_music_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freebeat',
            name='created',
            field=models.TimeField(default=datetime.datetime(2023, 5, 27, 9, 35, 31, 392172)),
        ),
        migrations.AlterField(
            model_name='music',
            name='created',
            field=models.TimeField(default=datetime.datetime(2023, 5, 27, 9, 35, 31, 392172)),
        ),
        migrations.AlterField(
            model_name='video',
            name='created',
            field=models.TimeField(default=datetime.datetime(2023, 5, 27, 9, 35, 31, 392172)),
        ),
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(upload_to='video'),
        ),
    ]
