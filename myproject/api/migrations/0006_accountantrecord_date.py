# Generated by Django 2.2.4 on 2019-08-18 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_accountantrecord_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountantrecord',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
