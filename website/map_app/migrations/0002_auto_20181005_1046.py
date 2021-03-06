# Generated by Django 2.1 on 2018-10-05 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='despesa',
            name='anulado',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
        migrations.AlterField(
            model_name='despesa',
            name='empenhado',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
        migrations.AlterField(
            model_name='despesa',
            name='liquidado',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
        migrations.AlterField(
            model_name='despesa',
            name='pago',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
        migrations.AlterField(
            model_name='localizacao',
            name='latitude',
            field=models.DecimalField(decimal_places=9, max_digits=12),
        ),
        migrations.AlterField(
            model_name='localizacao',
            name='longitude',
            field=models.DecimalField(decimal_places=9, max_digits=12),
        ),
    ]
