# Generated by Django 4.0.2 on 2022-07-02 18:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(default=datetime.datetime(2022, 7, 2, 18, 21, 12, 66703, tzinfo=utc))),
                ('completed', models.BooleanField(blank=True, default=False, null=True)),
                ('last_modified_at', models.DateTimeField(default=datetime.datetime(2022, 7, 2, 18, 21, 12, 66751, tzinfo=utc))),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
    ]
