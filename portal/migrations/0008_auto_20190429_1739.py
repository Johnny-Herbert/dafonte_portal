# Generated by Django 2.1.7 on 2019-04-29 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0007_memberlawyer_other_activities'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memberlawyer',
            name='other_activities',
            field=models.TextField(default='', verbose_name='Outras Atividades'),
        ),
    ]
