# Generated by Django 2.1.7 on 2019-07-30 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0033_auto_20190730_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opportunity',
            name='city',
            field=models.CharField(choices=[('RC', 'Recife-PE'), ('SL', 'Salvador-BA'), ('BS', 'Brasília-DF'), ('SP', 'São Paulo-SP')], default='RC', max_length=20, verbose_name='Cidade'),
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='city_en',
            field=models.CharField(choices=[('RC', 'Recife-PE'), ('SL', 'Salvador-BA'), ('BS', 'Brasília-DF'), ('SP', 'São Paulo-SP')], default='RC', max_length=20, null=True, verbose_name='Cidade'),
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='city_pt_br',
            field=models.CharField(choices=[('RC', 'Recife-PE'), ('SL', 'Salvador-BA'), ('BS', 'Brasília-DF'), ('SP', 'São Paulo-SP')], default='RC', max_length=20, null=True, verbose_name='Cidade'),
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='role',
            field=models.CharField(choices=[('LAWYER', 'Advogado'), ('INTERN', 'Estagiário'), ('TRAINEE', 'Trainee')], default='LAWYER', max_length=20, verbose_name='Cargo'),
        ),
    ]
