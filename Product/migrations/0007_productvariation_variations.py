# Generated by Django 3.1.4 on 2021-09-02 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0006_auto_20210902_1932'),
    ]

    operations = [
        migrations.AddField(
            model_name='productvariation',
            name='variations',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
