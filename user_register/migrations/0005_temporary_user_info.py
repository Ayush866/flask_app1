# Generated by Django 5.0 on 2023-12-21 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_register', '0004_alter_user_info_employee_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='temporary_user_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=200)),
                ('user_email', models.CharField(max_length=30)),
                ('user_token', models.CharField(max_length=300)),
            ],
        ),
    ]
