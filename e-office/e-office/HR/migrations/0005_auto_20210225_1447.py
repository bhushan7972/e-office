# Generated by Django 3.1.3 on 2021-02-25 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HR', '0004_auto_20210225_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='hr_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HR.hrp'),
        ),
    ]
