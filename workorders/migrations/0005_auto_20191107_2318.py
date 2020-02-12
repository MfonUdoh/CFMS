# Generated by Django 2.2.2 on 2019-11-07 23:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workorders', '0004_auto_20191107_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workorder',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='workorder',
            name='targetuser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='target', to=settings.AUTH_USER_MODEL),
        ),
    ]