# Generated by Django 2.1.7 on 2019-05-02 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0013_auto_20190502_1232'),
    ]

    operations = [
        migrations.AddField(
            model_name='pageparameter',
            name='description',
            field=models.TextField(blank=True, default='', verbose_name='Valor'),
        ),
    ]
