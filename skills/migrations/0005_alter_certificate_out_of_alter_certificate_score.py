# Generated by Django 5.0.6 on 2024-07-20 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0004_alter_certificate_out_of_alter_certificate_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='out_of',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='score',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
    ]
