# Generated by Django 2.1.2 on 2018-10-13 16:04

from django.db import migrations


def add_parsers(apps, schema_editor):
    Parser = apps.get_model("scrapes", "Parser")
    parsers = ["rrl latest", "rrl chapter", "rrl novel"]
    for p in parsers:
        Parser.objects.create(name=p)


def removeParsers(apps, schema_editor):
    Parser = apps.get_model("scrapes", "Parser")
    parsers = ["rrl latest", "rrl chapter", "rrl novel"]
    for p in parsers:
        Parser.objects.get(name=p).delete()


class Migration(migrations.Migration):

    dependencies = [("scrapes", "0003_delete_scrapegenerators")]

    operations = [migrations.RunPython(add_parsers, reverse_code=removeParsers)]
