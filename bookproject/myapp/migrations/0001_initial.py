# Generated by Django 4.2.3 on 2023-08-16 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tital', models.TextField()),
                ('Author', models.CharField(max_length=30)),
                ('Isbn', models.BigIntegerField()),
                ('Publisher', models.CharField(max_length=30)),
            ],
        ),
    ]
