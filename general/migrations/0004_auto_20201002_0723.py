# Generated by Django 2.2 on 2020-10-02 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0003_auto_20200930_0803'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='order',
        ),
        migrations.AddField(
            model_name='workout',
            name='order',
            field=models.TextField(blank=True, null=True),
        ),
    ]