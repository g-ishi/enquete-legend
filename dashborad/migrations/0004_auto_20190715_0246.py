# Generated by Django 2.2.3 on 2019-07-15 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashborad', '0003_auto_20190715_0230'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemTypeModel',
            fields=[
                ('item_type_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.AlterField(
            model_name='enquetemodel',
            name='delete_flag',
            field=models.BooleanField(default=False),
        ),
    ]
