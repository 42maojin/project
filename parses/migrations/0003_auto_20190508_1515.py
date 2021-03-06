# Generated by Django 2.2 on 2019-05-08 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parses', '0002_auto_20190508_0928'),
    ]

    operations = [
        migrations.CreateModel(
            name='ACCOUNT_GC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ACCOUNT_WC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='CONSUMPTION_WC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name_con', models.CharField(max_length=200)),
                ('account', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('plan_name', models.CharField(max_length=200)),
                ('unit_name', models.CharField(max_length=200)),
                ('key_word', models.CharField(max_length=200)),
                ('match_model', models.CharField(max_length=200)),
                ('bid', models.FloatField()),
                ('visit_url', models.TextField()),
                ('mobile_visit_url', models.TextField()),
                ('start_or_stop', models.CharField(max_length=100)),
                ('label', models.CharField(max_length=200)),
                ('applet', models.TextField()),
                ('key_word_status', models.CharField(max_length=100)),
                ('computer_price', models.CharField(max_length=200)),
                ('computer_quality', models.CharField(max_length=50)),
                ('mobile_quality', models.CharField(max_length=50)),
                ('consumption', models.FloatField()),
                ('avg_click_price', models.FloatField()),
                ('click_num', models.IntegerField()),
                ('show', models.IntegerField()),
                ('click_rate', models.CharField(max_length=200)),
                ('page_conversion', models.CharField(max_length=100)),
                ('k_show_consumption', models.CharField(max_length=100)),
                ('avg_conversion_price', models.CharField(max_length=200)),
                ('conversion_word', models.CharField(max_length=200)),
            ],
        ),
        migrations.RenameModel(
            old_name='CONSUMPTION',
            new_name='CONSUMPTION_GC',
        ),
        migrations.AlterField(
            model_name='file_name',
            name='create_time',
            field=models.DateTimeField(),
        ),
    ]
