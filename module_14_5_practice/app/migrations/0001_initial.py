# Generated by Django 4.2.7 on 2023-12-04 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PracticeModel',
            fields=[
                ('name', models.CharField(max_length=155)),
                ('auto', models.AutoField(primary_key=True, serialize=False)),
                ('big_int', models.BigIntegerField()),
                ('binary', models.BinaryField()),
                ('bol', models.BooleanField()),
                ('date', models.DateField()),
                ('dateTime', models.DateTimeField()),
                ('duration', models.DurationField()),
                ('ip', models.GenericIPAddressField()),
                ('json', models.JSONField()),
                ('slug', models.SlugField()),
                ('time', models.TimeField()),
                ('url', models.URLField()),
            ],
        ),
    ]