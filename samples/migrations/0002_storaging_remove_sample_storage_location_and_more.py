# Generated by Django 4.2.17 on 2024-12-23 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Storaging',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Location Name')),
                ('short_name', models.CharField(max_length=10, unique=True, verbose_name='Short Name')),
                ('type', models.CharField(max_length=100, verbose_name='Type')),
            ],
        ),
        migrations.RemoveField(
            model_name='sample',
            name='storage_location',
        ),
        migrations.AddField(
            model_name='sample',
            name='storaging',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='samples', to='samples.storaging', verbose_name='Storage Location'),
            preserve_default=False,
        ),
    ]