# Generated by Django 2.1 on 2018-10-05 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map_app', '0003_auto_20181005_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='despesa',
            name='descricao',
            field=models.TextField(),
        ),
    ]