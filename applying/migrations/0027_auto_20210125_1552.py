# Generated by Django 2.1.7 on 2021-01-25 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('applying', '0026_applicationlanguage_level'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='applicationlanguage',
            options={'ordering': ['language'], 'verbose_name': 'idioma', 'verbose_name_plural': 'idiomas'},
        ),
    ]
