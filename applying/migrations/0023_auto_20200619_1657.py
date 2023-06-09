# Generated by Django 2.1.7 on 2020-06-19 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('applying', '0022_auto_20190910_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academic',
            name='period',
            field=models.CharField(blank=True, choices=[('X', 'Concluído'), ('1', '1º Período'), ('2', '2º Período'), ('3', '3º Período'), ('4', '4º Período'), ('5', '5º Período'), ('6', '6º Período'), ('7', '7º Período'), ('8', '8º Período'), ('9', '9º Período'), ('10', '10º Período'), ('12', '12º Período')], max_length=20, verbose_name='Período'),
        ),
        migrations.AlterField(
            model_name='academic',
            name='shift',
            field=models.CharField(blank=True, choices=[('X', 'Concluído'), ('M', 'Manhã'), ('T', 'Tarde'), ('N', 'Noite')], max_length=20, verbose_name='Turno'),
        ),
        migrations.AlterField(
            model_name='application',
            name='opportunity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='related_applications', to='portal.Opportunity'),
        ),
        migrations.AlterField(
            model_name='application',
            name='practice_areas',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='related_applications', to='portal.PracticeArea'),
        ),
        migrations.AlterField(
            model_name='application',
            name='specialization_sectors',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='related_applications', to='portal.SpecializationSector'),
        ),
    ]
