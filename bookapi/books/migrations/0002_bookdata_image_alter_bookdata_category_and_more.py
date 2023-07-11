# Generated by Django 4.2.3 on 2023-07-10 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookdata',
            name='image',
            field=models.ImageField(default='images/none/notfound.png', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='bookdata',
            name='category',
            field=models.CharField(default='none', max_length=128),
        ),
        migrations.AlterField(
            model_name='bookdata',
            name='rating',
            field=models.FloatField(max_length=128),
        ),
    ]