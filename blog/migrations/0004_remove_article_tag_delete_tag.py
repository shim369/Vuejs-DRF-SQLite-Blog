# Generated by Django 4.1.4 on 2022-12-29 04:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_article_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='tag',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]