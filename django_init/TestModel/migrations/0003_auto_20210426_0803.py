# Generated by Django 3.2 on 2021-04-26 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestModel', '0002_auto_20210426_0802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='field',
            field=models.JSONField(blank=True, null=True, verbose_name='field'),
        ),
        migrations.AlterField(
            model_name='test',
            name='field_desc',
            field=models.JSONField(blank=True, null=True, verbose_name='field_desc'),
        ),
        migrations.AlterField(
            model_name='test',
            name='tag',
            field=models.JSONField(blank=True, null=True, verbose_name='tag'),
        ),
        migrations.AlterField(
            model_name='test',
            name='tag_desc',
            field=models.JSONField(blank=True, null=True, verbose_name='tag_desc'),
        ),
    ]
