# Generated by Django 4.1.7 on 2023-03-19 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_alter_profile_gender_alter_profile_userrole'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male')], default='F', max_length=1),
        ),
        migrations.AlterField(
            model_name='profile',
            name='userRole',
            field=models.CharField(choices=[('I', 'Instructor'), ('S', 'Student')], default='I', max_length=1),
        ),
    ]
