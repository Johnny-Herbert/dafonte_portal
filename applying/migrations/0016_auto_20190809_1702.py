# Generated by Django 2.1.7 on 2019-08-09 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applying', '0015_auto_20190809_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='role',
            field=models.CharField(blank=True, choices=[('LAWYER', 'Advogado'), ('INTERN', 'Estagiário'), ('SUPPORT', 'Equipe de apoio')], max_length=20, verbose_name='Cargo'),
        ),
    ]