# Generated by Django 4.2.3 on 2023-07-26 05:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_create_signup_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='created',
        ),
    ]