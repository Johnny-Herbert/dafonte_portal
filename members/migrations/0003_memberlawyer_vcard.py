# Generated by Django 2.1.7 on 2019-05-03 01:03

import dafonte_portal.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_proxyadministrativestaff_proxyintern_proxylawyer_proxytrainee'),
    ]

    operations = [
        migrations.AddField(
            model_name='memberlawyer',
            name='vcard',
            field=models.FileField(blank=True, null=True, upload_to=dafonte_portal.utils.upload_to),
        ),
    ]
