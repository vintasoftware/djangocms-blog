# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations
from django.utils.html import strip_tags


def migrate_meta_description(apps, schema_editor):
    PostTranslation = apps.get_model("djangocms_blog", "PostTranslation")
    abstract_default = PostTranslation._meta.get_field('abstract').get_default()
    for post in PostTranslation.objects.all():
        post.meta_description = strip_tags(post.abstract)
        post.abstract = abstract_default
        post.save()


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_blog', '0021_auto_20160708_1850'),
    ]

    operations = [
        migrations.RunPython(migrate_meta_description),
    ]
