# Generated by Django 5.1.5 on 2025-04-07 17:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubes', '0003_solicitudmembresia_miembroclub'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='horario',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.CreateModel(
            name='Reunion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('ubicacion', models.CharField(blank=True, max_length=255, null=True)),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reuniones', to='clubes.club')),
            ],
        ),
    ]
