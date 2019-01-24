# Generated by Django 2.1.5 on 2019-01-13 14:04

from django.db import migrations
from django.db.models import Subquery as _Subquery, OuterRef as _OuterRef, F as _F


def convertToPercentage(apps, schema):
    _ReadingProgress = apps.get_model("profiles", "ReadingProgress")
    _Chapter = apps.get_model("novels", "Chapter")

    sq = _Subquery(
        _Chapter.objects.filter(id=_OuterRef("chapter_id")).values("total_progress")
    )
    _ReadingProgress.objects.update(progress=_F("progress") / sq * 100)


def convertToAbsolutes(apps, schema):
    _ReadingProgress = apps.get_model("profiles", "ReadingProgress")
    _Chapter = apps.get_model("novels", "Chapter")

    sq = _Subquery(
        _Chapter.objects.filter(id=_OuterRef("chapter_id")).values("total_progress")
    )
    _ReadingProgress.objects.update(progress=_F("progress") * sq / 100)


class Migration(migrations.Migration):

    dependencies = [("profiles", "0010_unique_together")]

    operations = [
        migrations.RunPython(convertToPercentage, reverse_code=convertToAbsolutes)
    ]
