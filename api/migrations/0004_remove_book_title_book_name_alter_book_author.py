# Generated by Django 5.0.7 on 2024-07-15 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_book_author_remove_book_genre_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='title',
        ),
        migrations.AddField(
            model_name='book',
            name='name',
            field=models.CharField(default=0, max_length=200, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
