# Generated by Django 3.2.7 on 2021-09-20 02:24

from django.db import migrations, models
import skins.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Skin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.CharField(blank=True, max_length=256, null=True)),
                ('skin_type', models.CharField(choices=[('1', 'Low res'), ('2', 'High res')], max_length=1)),
                ('motif', models.CharField(blank=True, max_length=64, null=True)),
                ('skin_id', models.CharField(max_length=16)),
                ('image', models.ImageField(upload_to=skins.models.Skin.get_skin_image_path)),
            ],
        ),
    ]
