# Generated by Django 5.1.4 on 2025-02-08 22:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create_qr_code', '0009_alter_qrcodes_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='qrcodes',
            name='logo',
            field=models.TextField(default='none'),
        ),
        migrations.AlterField(
            model_name='qrcodes',
            name='date',
            field=models.DateField(default=datetime.date(2025, 2, 9)),
        ),
    ]
