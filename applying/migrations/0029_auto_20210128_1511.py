# Generated by Django 2.1.7 on 2021-01-28 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('applying', '0028_application_is_downloaded'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='practice_areas',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='related_applications', to='portal.PracticeArea', verbose_name='Área de Atuação'),
        ),
        migrations.AlterField(
            model_name='application',
            name='specialization_sectors',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='related_applications', to='portal.SpecializationSector', verbose_name='Setor de Especialização'),
        ),
    ]
