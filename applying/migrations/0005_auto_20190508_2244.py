# Generated by Django 2.1.7 on 2019-05-09 01:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('applying', '0004_auto_20190508_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='opportunity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='related_applications', to='portal.Opportunity'),
        ),
        migrations.AlterField(
            model_name='professionalexperience',
            name='date_begin',
            field=models.DateField(blank=True, null=None, verbose_name='Data de Inicio'),
        ),
        migrations.AlterField(
            model_name='professionalexperience',
            name='date_finish',
            field=models.DateField(blank=True, null=None, verbose_name='Data de término'),
        ),
    ]
