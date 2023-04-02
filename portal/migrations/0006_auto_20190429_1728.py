# Generated by Django 2.1.7 on 2019-04-29 20:28

import ckeditor_uploader.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal','0005_memberlawyer_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='AwardMembers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='files/', verbose_name='Imagem')),
                ('publication_date', models.DateField(default=datetime.datetime.now, verbose_name='Data de Publicação')),
                ('title', models.CharField(default='', max_length=100, verbose_name='Título')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(default='', max_length=100, verbose_name='Descrição')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='portal.MemberLawyer')),
            ],
            options={
                'verbose_name': 'prêmio do membro',
            },
        ),
    ]
