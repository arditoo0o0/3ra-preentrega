# Generated by Django 5.0.7 on 2024-08-02 00:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appcoder', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estudiante',
            old_name='apellido',
            new_name='contraseña',
        ),
        migrations.RemoveField(
            model_name='estudiante',
            name='email',
        ),
    ]
