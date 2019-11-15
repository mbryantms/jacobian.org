# Generated by Django 2.1.3 on 2018-11-09 19:20

from django.db import migrations
import django_postgres_unlimited_varchar


class Migration(migrations.Migration):

    dependencies = [("speaking_portfolio", "0001_initial")]

    operations = [
        migrations.AddField(
            model_name="presentation",
            name="type",
            field=django_postgres_unlimited_varchar.UnlimitedCharField(
                choices=[
                    ("keynote", "Keynote"),
                    ("talk", "Talk"),
                    ("tutorial", "Tutorial"),
                ],
                default="talk",
            ),
        )
    ]
