# Generated by Django 2.2 on 2020-09-15 22:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0004_auto_20200915_1715'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='workout',
            options={'ordering': ('datetime',)},
        ),
    ]