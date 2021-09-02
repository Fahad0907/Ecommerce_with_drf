# Generated by Django 3.1.4 on 2021-09-02 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0009_auto_20210902_1940'),
    ]

    operations = [
        migrations.CreateModel(
            name='Variation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variationtype', models.CharField(max_length=50)),
                ('value', models.CharField(max_length=50)),
                ('productID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Product.productdetails')),
            ],
        ),
    ]
