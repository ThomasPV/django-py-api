# Generated by Django 2.2 on 2019-05-02 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_user_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='phone_number',
        ),
    ]
