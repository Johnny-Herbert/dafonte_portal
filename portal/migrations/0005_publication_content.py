# Generated by Django 2.1.7 on 2019-04-29 19:53

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0004_auto_20190426_1417'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]
