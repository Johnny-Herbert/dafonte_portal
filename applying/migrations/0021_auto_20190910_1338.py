# Generated by Django 2.1.7 on 2019-09-10 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applying', '0020_professionalexperience_intend_area'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='professionalexperience',
            name='intend_area',
        ),
        migrations.AddField(
            model_name='application',
            name='intend_area',
            field=models.TextField(blank=True, verbose_name='Área Pretendida'),
        ),
    ]