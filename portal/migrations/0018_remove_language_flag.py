# Generated by Django 2.1.7 on 2019-05-02 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0017_auto_20190502_1456'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='language',
            name='flag',
        ),
    ]
