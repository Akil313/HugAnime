# Generated by Django 2.0.3 on 2018-04-05 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_remove_animecatalog_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animecatalog',
            name='anime_id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
