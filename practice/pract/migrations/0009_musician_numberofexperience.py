# Generated by Django 3.2.5 on 2021-07-25 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pract', '0008_alter_musician_first_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='musician',
            name='numberOfExperience',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
