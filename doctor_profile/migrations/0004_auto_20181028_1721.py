# Generated by Django 2.1.2 on 2018-10-28 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor_profile', '0003_profile_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='userid',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
