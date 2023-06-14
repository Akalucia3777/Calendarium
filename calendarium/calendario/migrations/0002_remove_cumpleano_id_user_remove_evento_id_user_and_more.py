# Generated by Django 4.2.1 on 2023-06-14 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendario', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cumpleano',
            name='id_user',
        ),
        migrations.RemoveField(
            model_name='evento',
            name='id_user',
        ),
        migrations.RemoveField(
            model_name='tarea',
            name='id_user',
        ),
        migrations.RemoveField(
            model_name='tracker',
            name='id_user',
        ),
        migrations.AddField(
            model_name='tracker',
            name='realizado',
            field=models.CharField(default='0', max_length=1),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='priority',
            field=models.CharField(max_length=255),
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
