# Generated by Django 2.1.4 on 2018-12-30 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("profiles", "0008_auto_20181229_1637")]

    operations = [
        migrations.AddField(
            model_name="readingprogress",
            name="timestamp",
            field=models.DateTimeField(auto_now=True),
        )
    ]