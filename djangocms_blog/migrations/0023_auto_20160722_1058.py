# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations
from django.utils.html import strip_tags


def migrate_abstract(apps, schema_editor):
    PostTranslation = apps.get_model("djangocms_blog", "PostTranslation")
    for post in PostTranslation.objects.all():
        post.abstract = strip_tags(post.post_text)[:350]
        post.save()


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_blog', '0022_auto_20160711_1411'),
    ]

    operations = [
        migrations.RunPython(migrate_abstract),
    ]
