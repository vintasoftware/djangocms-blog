# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_blog', '0017_thumbnail_move'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='main_image_full',
            field=models.ForeignKey(related_name='djangocms_blog_post_full', on_delete=django.db.models.deletion.SET_NULL, verbose_name='main image full', blank=True, to='cmsplugin_filer_image.ThumbnailOption', null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='main_image_thumbnail',
            field=models.ForeignKey(related_name='djangocms_blog_post_thumbnail', on_delete=django.db.models.deletion.SET_NULL, verbose_name='main image thumbnail', blank=True, to='cmsplugin_filer_image.ThumbnailOption', null=True),
        ),
    ]
