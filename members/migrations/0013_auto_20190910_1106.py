# Generated by Django 2.1.7 on 2019-09-10 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0034_auto_20190730_1848'),
        ('members', '0012_auto_20190730_1607'),
    ]

    operations = [
        migrations.AddField(
            model_name='memberintern',
            name='specialization_sectors',
            field=models.ManyToManyField(related_name='interns', to='portal.SpecializationSector'),
        ),
        migrations.AddField(
            model_name='membertrainee',
            name='specialization_sectors',
            field=models.ManyToManyField(related_name='trainees', to='portal.SpecializationSector'),
        ),
    ]
