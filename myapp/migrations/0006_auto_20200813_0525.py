# Generated by Django 3.1 on 2020-08-12 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20200813_0339'),
    ]

    operations = [
        migrations.AddField(
            model_name='resumedata',
            name='Certification2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='Certificationlink2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='JobDescription',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='JobDescription2',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='Skill4',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='Softskill1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='Softskill2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='Softskill3',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='Softskill4',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='resumedata',
            name='Jobstate',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='resumedata',
            name='created_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]