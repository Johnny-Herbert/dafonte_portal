# Generated by Django 2.1.7 on 2019-05-02 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0016_remove_pageparameter_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pageparameter',
            name='file',
        ),
        migrations.RemoveField(
            model_name='pageparameter',
            name='file_en',
        ),
        migrations.RemoveField(
            model_name='pageparameter',
            name='file_pt_br',
        ),
    ]
