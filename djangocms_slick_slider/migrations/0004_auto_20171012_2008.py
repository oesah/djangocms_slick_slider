# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-10-12 18:08
from __future__ import unicode_literals

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_slick_slider', '0003_remove_slickslider_slick_settings'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='slicksliderimage',
            options={'verbose_name': 'Slider Image', 'verbose_name_plural': 'Slider Images'},
        ),
        migrations.AddField(
            model_name='slickslider',
            name='arrow_color',
            field=models.CharField(default='#ddd', help_text='Define the color of slider arrows here. All CSS color values work (e.g. #efefef)', max_length=255, verbose_name='Arrow color'),
        ),
        migrations.AlterField(
            model_name='slickslider',
            name='settings',
            field=jsonfield.fields.JSONField(default=b'\n{\n  "dots":true,\n  "slidesToShow":4,\n  "mobileFirst":true,\n  "slidesToScroll":4\n}\n', verbose_name='Slick settings'),
        ),
    ]