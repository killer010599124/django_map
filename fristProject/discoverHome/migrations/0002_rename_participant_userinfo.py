# Generated by Django 4.1.6 on 2023-02-05 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("discoverHome", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(old_name="Participant", new_name="UserInfo",),
    ]
