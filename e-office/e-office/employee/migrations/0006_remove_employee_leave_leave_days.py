# Generated by Django 3.1.4 on 2021-02-10 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0005_auto_20210210_1604'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee_leave',
            name='leave_days',
        ),
    ]
