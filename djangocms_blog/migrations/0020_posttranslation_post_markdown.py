# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_blog', '0019_latestpostsplugin_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='posttranslation',
            name='post_markdown',
            field=models.TextField(blank=True, verbose_name='markdown', default=''),
        ),
    ]
