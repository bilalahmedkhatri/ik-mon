# Generated by Django 4.2.4 on 2024-05-12 04:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0002_mainuser_contact_mainuser_doi_mainuser_location_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="mainuser",
            name="os_name",
            field=models.CharField(default="", max_length=100, verbose_name="OS Name"),
        ),
        migrations.AddField(
            model_name="mainuser",
            name="system_start_time",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AddField(
            model_name="mainuser",
            name="token",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AlterField(
            model_name="mainuser",
            name="contact",
            field=models.IntegerField(default=0, verbose_name="Contact"),
        ),
    ]