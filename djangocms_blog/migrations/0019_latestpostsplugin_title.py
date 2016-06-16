# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_blog', '0018_auto_20160603_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='latestpostsplugin',
            name='title',
            field=djangocms_text_ckeditor.fields.HTMLField(verbose_name='Title', blank=True),
        ),
    ]
