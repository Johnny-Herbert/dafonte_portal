# Generated by Django 2.1.7 on 2019-05-09 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0010_auto_20190507_1941'),
    ]

    operations = [
        migrations.AddField(
            model_name='memberintern',
            name='sex',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], default='', max_length=1),
        ),
    ]
