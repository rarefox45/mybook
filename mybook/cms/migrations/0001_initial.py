# Generated by Django 2.0.2 on 2018-03-15 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Impression',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, verbose_name='コメント')),
            ],
        ),
        migrations.CreateModel(
            name='Kanmusu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipname', models.CharField(max_length=255, verbose_name='艦名')),
                ('shipclass', models.CharField(blank=True, max_length=255, verbose_name='艦種')),
                ('shiplevel', models.IntegerField(blank=True, default=1, verbose_name='レベル')),
            ],
        ),
        migrations.AddField(
            model_name='impression',
            name='ship',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='impressions', to='cms.Kanmusu', verbose_name='艦娘'),
        ),
    ]