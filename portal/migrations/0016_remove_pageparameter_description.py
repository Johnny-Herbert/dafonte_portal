# Generated by Django 2.1.7 on 2019-05-02 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0015_auto_20190502_1442'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pageparameter',
            name='description',
        ),
    ]
