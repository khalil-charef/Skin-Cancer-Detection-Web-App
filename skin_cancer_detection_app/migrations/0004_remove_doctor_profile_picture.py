# Generated by Django 5.1.3 on 2024-11-30 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skin_cancer_detection_app', '0003_doctor_appointment_url_doctor_contact_url_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='profile_picture',
        ),
    ]