# Generated by Django 4.1.6 on 2023-02-21 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0011_alter_book_authors_alter_book_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='is_archived',
            field=models.BooleanField(default=False, null=True),
        ),
    ]