# Generated by Django 3.2.5 on 2021-07-25 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pract', '0007_alter_musician_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musician',
            name='first_name',
            field=models.CharField(db_column='Musician First Name', db_index=True, max_length=50),
        ),
    ]
