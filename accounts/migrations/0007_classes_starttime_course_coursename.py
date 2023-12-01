# Generated by Django 4.2.5 on 2023-12-01 02:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_classes_checkincode'),
    ]

    operations = [
        migrations.AddField(
            model_name='classes',
            name='starttime',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='courseName',
            field=models.CharField(default='Name', max_length=32),
            preserve_default=False,
        ),
    ]