# Generated by Django 5.0 on 2023-12-19 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_register', '0003_remove_user_info_id_alter_user_info_employee_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_info',
            name='employee_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]