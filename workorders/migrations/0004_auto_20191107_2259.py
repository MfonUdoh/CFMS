# Generated by Django 2.2.2 on 2019-11-07 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workorders', '0003_workorder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workorder',
            name='targetuser',
            field=models.CharField(max_length=200),
        ),
    ]