# Generated by Django 4.0.4 on 2024-07-24 17:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Medicine_app', '0008_alter_signup_age_alter_signup_dob_alter_signup_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='age',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='signup',
            name='dob',
            field=models.DateField(default=datetime.date.today),
        ),
    ]