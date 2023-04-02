# Generated by Django 2.1.7 on 2019-07-30 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applying', '0007_auto_20190730_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='local',
            field=models.CharField(blank=True, choices=[('OP', 'Olhar oportunidade'), ('RC', 'Recife'), ('SL', 'Salvador'), ('BS', 'Brasília'), ('SP', 'São Paulo')], max_length=1, verbose_name='Localidade'),
        ),
        migrations.AlterField(
            model_name='application',
            name='role',
            field=models.CharField(blank=True, choices=[('OPORTUNITY', 'Olhar oportunidade'), ('LAWYER', 'Advogado'), ('INTERN', 'Estagiário'), ('TRAINEE', 'Trainee')], max_length=1, verbose_name='Cargo'),
        ),
    ]