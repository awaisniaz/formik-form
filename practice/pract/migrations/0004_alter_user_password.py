# Generated by Django 3.2.5 on 2021-07-23 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pract', '0003_alter_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=200, verbose_name='Enter Password'),
        ),
    ]