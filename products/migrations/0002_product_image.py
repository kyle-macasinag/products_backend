# Generated by Django 4.0.4 on 2022-04-14 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
