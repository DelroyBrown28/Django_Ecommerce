# Generated by Django 3.1.1 on 2021-05-06 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepagecustomisation',
            name='home_page_title',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
