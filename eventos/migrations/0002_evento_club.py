# Generated by Django 4.2.11 on 2025-04-04 06:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clubes', '0003_solicitudmembresia_miembroclub'),
        ('eventos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='club',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clubes.club'),
        ),
    ]
