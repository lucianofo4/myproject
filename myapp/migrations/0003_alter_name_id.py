# Generated by Django 3.2.2 on 2022-05-28 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20220528_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='name',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
