# Generated by Django 3.1.7 on 2021-07-18 03:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anne', '0010_commment'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Commment',
            new_name='Comment',
        ),
    ]
