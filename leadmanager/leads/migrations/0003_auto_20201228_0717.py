# Generated by Django 3.0.5 on 2020-12-28 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0002_lead_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lead',
            old_name='author',
            new_name='owner',
        ),
    ]
