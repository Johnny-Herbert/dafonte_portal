# Generated by Django 2.1.7 on 2019-04-30 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Academic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=50, verbose_name='Curso')),
                ('institution', models.CharField(max_length=100, verbose_name='Instituição')),
                ('conclusion', models.IntegerField(verbose_name='Ano de conclusão')),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nome')),
                ('email', models.CharField(max_length=50, verbose_name='E-mail')),
                ('phone', models.CharField(default='', max_length=19, verbose_name='Telefone')),
                ('address', models.TextField(verbose_name='Address')),
                ('extra_qualification', models.TextField(default='', verbose_name='Qualificações e atividades complementares')),
            ],
        ),
        migrations.CreateModel(
            name='ApplicationLanguage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=30, verbose_name='Idioma')),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_idioms', to='applying.Application')),
            ],
        ),
        migrations.CreateModel(
            name='ProfessionalExperience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enterprise', models.CharField(max_length=50, verbose_name='Empresa')),
                ('function', models.CharField(max_length=50, verbose_name='Cargo')),
                ('area', models.CharField(max_length=50, verbose_name='Area')),
                ('periodo', models.CharField(max_length=150, verbose_name='Periodo')),
                ('activities', models.TextField(verbose_name='Principais atividades desenvolvidas')),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_professional', to='applying.Application')),
            ],
        ),
        migrations.AddField(
            model_name='academic',
            name='application',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_academic', to='applying.Application'),
        ),
    ]
