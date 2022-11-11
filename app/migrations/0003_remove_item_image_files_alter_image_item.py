# Generated by Django 4.1.3 on 2022-11-11 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_images_item_image_files_alter_image_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='image_files',
        ),
        migrations.AlterField(
            model_name='image',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.item'),
        ),
    ]