# Generated by Django 3.1.5 on 2021-02-05 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moderator', '0003_auto_20210205_0002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='title',
        ),
        migrations.AddField(
            model_name='store',
            name='notification_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
