# Generated by Django 2.0.7 on 2018-11-12 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0007_auto_20181110_0053'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='github_username',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]