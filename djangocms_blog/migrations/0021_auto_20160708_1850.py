# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import markdown


def migrate_markdown(apps, schema_editor):
    markdown_extensions = ['markdown.extensions.fenced_code',
                           'markdown.extensions.codehilite']
    PostTranslation = apps.get_model("djangocms_blog", "PostTranslation")
    for post in PostTranslation.objects.all():
        plugin = post.master.content.cmsplugin_set.first()
        markdown_text = plugin.markdownplugin.markdown_text
        post.post_markdown = markdown_text
        post.post_text = markdown.markdown(markdown_text,
                                           extensions=markdown_extensions)
        post.save()


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_blog', '0020_posttranslation_post_markdown'),
    ]

    operations = [
        migrations.RunPython(migrate_markdown),
    ]
