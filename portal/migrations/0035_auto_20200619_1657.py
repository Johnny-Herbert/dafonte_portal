# Generated by Django 2.1.7 on 2020-06-19 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0034_auto_20190730_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='office',
            name='address',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Endereço'),
        ),
        migrations.AlterField(
            model_name='office',
            name='address_en',
            field=models.CharField(blank=True, default='', max_length=200, null=True, verbose_name='Endereço'),
        ),
        migrations.AlterField(
            model_name='office',
            name='address_pt_br',
            field=models.CharField(blank=True, default='', max_length=200, null=True, verbose_name='Endereço'),
        ),
        migrations.AlterField(
            model_name='office',
            name='city',
            field=models.CharField(blank=True, default='', max_length=50, verbose_name='Cidade'),
        ),
        migrations.AlterField(
            model_name='office',
            name='city_en',
            field=models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='Cidade'),
        ),
        migrations.AlterField(
            model_name='office',
            name='city_pt_br',
            field=models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='Cidade'),
        ),
        migrations.AlterField(
            model_name='office',
            name='country',
            field=models.CharField(blank=True, default='Brasil', max_length=50, verbose_name='País'),
        ),
        migrations.AlterField(
            model_name='office',
            name='country_en',
            field=models.CharField(blank=True, default='Brasil', max_length=50, null=True, verbose_name='País'),
        ),
        migrations.AlterField(
            model_name='office',
            name='country_pt_br',
            field=models.CharField(blank=True, default='Brasil', max_length=50, null=True, verbose_name='País'),
        ),
        migrations.AlterField(
            model_name='office',
            name='email',
            field=models.CharField(blank=True, default='', max_length=50, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='office',
            name='gmaps_iframe',
            field=models.CharField(blank=True, default='', max_length=500, verbose_name='Iframe Embbedado do Google'),
        ),
        migrations.AlterField(
            model_name='office',
            name='neighborhood',
            field=models.CharField(blank=True, default='', max_length=50, verbose_name='Bairro'),
        ),
        migrations.AlterField(
            model_name='office',
            name='neighborhood_en',
            field=models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='Bairro'),
        ),
        migrations.AlterField(
            model_name='office',
            name='neighborhood_pt_br',
            field=models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='Bairro'),
        ),
        migrations.AlterField(
            model_name='office',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=19, verbose_name='Telefone'),
        ),
        migrations.AlterField(
            model_name='office',
            name='postcode',
            field=models.CharField(blank=True, default='', max_length=10, verbose_name='CEP'),
        ),
        migrations.AlterField(
            model_name='office',
            name='state',
            field=models.CharField(blank=True, default='', max_length=50, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='office',
            name='state_en',
            field=models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='office',
            name='state_pt_br',
            field=models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='practicearea',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='practicearea',
            name='name_en',
            field=models.CharField(max_length=100, null=True, unique=True, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='practicearea',
            name='name_pt_br',
            field=models.CharField(max_length=100, null=True, unique=True, verbose_name='Nome'),
        ),
    ]
