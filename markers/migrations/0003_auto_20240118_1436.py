# Generated by Django 3.2.23 on 2024-01-18 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('markers', '0002_auto_20240118_1133'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='evcharginglocation',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='markers.category'),
        ),
    ]
