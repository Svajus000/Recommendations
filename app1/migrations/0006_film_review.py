# Generated by Django 5.0.6 on 2024-09-17 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_user_film_list_recommendations'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='review',
            field=models.CharField(default=''),
        ),
    ]