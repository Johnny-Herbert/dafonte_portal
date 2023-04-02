# Generated by Django 2.1.7 on 2019-04-30 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0024_auto_20190502_2001'),
        ('applying', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='academic',
            options={'verbose_name': 'formação acadêmica', 'verbose_name_plural': 'formações acadêmicas'},
        ),
        migrations.AlterModelOptions(
            name='application',
            options={'verbose_name': 'currículo', 'verbose_name_plural': 'currículos'},
        ),
        migrations.AlterModelOptions(
            name='applicationlanguage',
            options={'verbose_name': 'idioma', 'verbose_name_plural': 'idiomas'},
        ),
        migrations.AlterModelOptions(
            name='professionalexperience',
            options={'verbose_name': 'experiência profissional', 'verbose_name_plural': 'experiências profissionais'},
        ),
        migrations.AddField(
            model_name='application',
            name='opportunity',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='related_application', to='portal.Opportunity'),
            preserve_default=False,
        ),
    ]