# Generated by Django 3.1 on 2020-08-13 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20200813_0526'),
    ]

    operations = [
        migrations.AddField(
            model_name='resumedata',
            name='About',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]