# Generated by Django 3.1.4 on 2021-09-02 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0007_productvariation_variations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productvariation',
            name='type',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
