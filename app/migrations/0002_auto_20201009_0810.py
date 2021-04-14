# Generated by Django 2.2.10 on 2020-10-09 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='good',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='good',
            name='interesting',
        ),
        migrations.AddField(
            model_name='cart',
            name='good',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Good'),
        ),
        migrations.AddField(
            model_name='interesting',
            name='good',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Good'),
        ),
    ]