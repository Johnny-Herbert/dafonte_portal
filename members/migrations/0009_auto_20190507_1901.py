# Generated by Django 2.1.7 on 2019-05-07 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0008_auto_20190507_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memberlawyer',
            name='awards',
            field=models.ManyToManyField(blank=True, related_name='lawyers', to='members.AwardMembers', verbose_name='Prêmios'),
        ),
    ]
