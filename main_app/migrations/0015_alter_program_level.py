# Generated by Django 4.1.7 on 2023-03-22 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0014_registeredstudent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='level',
            field=models.CharField(choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Expert', 'Expert')], default=0, max_length=12),
        ),
    ]