# Generated by Django 3.0.2 on 2020-04-19 22:07

from django.db import migrations

def forwards_func(apps, schema_editor):
    Settings = apps.get_model("djgentelella", "GentelellaSettings")
    Settings.objects.create(
        key='site_title',
        value='Django Gentelella Alela!'
    )

class Migration(migrations.Migration):

    dependencies = [
        ('djgentelella', '0003_help'),
    ]

    operations = [
        migrations.RunPython(forwards_func)
    ]
