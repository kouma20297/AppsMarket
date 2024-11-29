# Generated by Django 3.2.22 on 2024-11-29 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('last_name', models.CharField(default='Unknown', max_length=100)),
                ('first_name', models.CharField(default='Unknown', max_length=100)),
                ('phone_number', models.CharField(max_length=15, unique=True)),
                ('password_hash', models.CharField(default='', max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'User',
                'db_table': 'user',
            },
        ),
    ]
