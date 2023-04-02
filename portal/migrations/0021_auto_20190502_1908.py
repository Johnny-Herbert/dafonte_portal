# Generated by Django 2.1.7 on 2019-05-02 22:08

import dafonte_portal.utils
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0020_alter_members_tables'),
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='affiliate',
            name='logo',
            field=models.ImageField(upload_to=dafonte_portal.utils.upload_to, verbose_name='Logo'),
        ),
        migrations.AlterField(
            model_name='award',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=dafonte_portal.utils.upload_to, verbose_name='Imagem'),
        ),
        migrations.AlterField(
            model_name='awardmembers',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='members.MemberLawyer'),
        ),
        migrations.AlterField(
            model_name='awardmembers',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=dafonte_portal.utils.upload_to, verbose_name='Imagem'),
        ),
        migrations.AlterField(
            model_name='event',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=dafonte_portal.utils.upload_to, verbose_name='Capa do evento'),
        ),
        migrations.AlterField(
            model_name='event',
            name='related_events_lawyers',
            field=models.ManyToManyField(blank=True, related_name='related_events_lawyers', to='members.MemberLawyer', verbose_name='Advogados Relacionados'),
        ),
        migrations.AlterField(
            model_name='event',
            name='related_events_trainees',
            field=models.ManyToManyField(blank=True, related_name='related_events_trainees', to='members.MemberTrainee', verbose_name='Trainees Relacionados'),
        ),
        migrations.AlterField(
            model_name='page',
            name='background_image',
            field=models.ImageField(blank=True, null=True, upload_to=dafonte_portal.utils.upload_to, verbose_name='Imagem de Fundo'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='logo',
            field=models.ImageField(upload_to=dafonte_portal.utils.upload_to, verbose_name='Logo'),
        ),
        migrations.AlterField(
            model_name='practicearea',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=dafonte_portal.utils.upload_to, verbose_name='Imagem'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='file',
            field=models.FileField(blank=True, default='', max_length=50, null=True, upload_to=dafonte_portal.utils.upload_to, verbose_name='Anexo PDF'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='file_en',
            field=models.FileField(blank=True, default='', max_length=50, null=True, upload_to=dafonte_portal.utils.upload_to, verbose_name='Anexo PDF'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='file_pt_br',
            field=models.FileField(blank=True, default='', max_length=50, null=True, upload_to=dafonte_portal.utils.upload_to, verbose_name='Anexo PDF'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=dafonte_portal.utils.upload_to, verbose_name='Capa da publicação'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='related_members',
            field=models.ManyToManyField(blank=True, related_name='related_publications', to='members.Member', verbose_name='Membros Relacionados'),
        ),
        migrations.AlterField(
            model_name='siteparameter',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=dafonte_portal.utils.upload_to, verbose_name='Arquivo'),
        ),
        migrations.AlterField(
            model_name='siteparameter',
            name='file_en',
            field=models.FileField(blank=True, null=True, upload_to=dafonte_portal.utils.upload_to, verbose_name='Arquivo'),
        ),
        migrations.AlterField(
            model_name='siteparameter',
            name='file_pt_br',
            field=models.FileField(blank=True, null=True, upload_to=dafonte_portal.utils.upload_to, verbose_name='Arquivo'),
        ),
        migrations.AlterField(
            model_name='socialentity',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=dafonte_portal.utils.upload_to, verbose_name='Logo da entidade social'),
        ),
        migrations.AlterField(
            model_name='specializationsector',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=dafonte_portal.utils.upload_to, verbose_name='Capa da página'),
        ),
    ]
