# Generated by Django 5.0.6 on 2024-06-04 11:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testbo', '0002_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='testbo.post'),
        ),
    ]
