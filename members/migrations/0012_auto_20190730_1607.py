# Generated by Django 2.1.7 on 2019-07-30 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0011_memberintern_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memberlawyer',
            name='practice_areas',
            field=models.ManyToManyField(blank=True, related_name='lawyers', to='portal.PracticeArea', verbose_name='Áreas de Atuação'),
        ),
    ]
