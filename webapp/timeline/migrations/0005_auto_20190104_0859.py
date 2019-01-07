# Generated by Django 2.1.4 on 2019-01-04 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0004_auto_20190103_1138'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('document', models.FileField(upload_to='documents/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Document',
            },
        ),
        migrations.RemoveField(
            model_name='like',
            name='post',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]
