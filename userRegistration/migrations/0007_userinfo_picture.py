# Generated by Django 3.2 on 2021-05-17 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userRegistration', '0006_auto_20210429_0200'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='picture',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
