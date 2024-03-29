# Generated by Django 2.2.3 on 2019-07-15 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashborad', '0002_auto_20190715_0218'),
    ]

    operations = [
        migrations.AddField(
            model_name='enquetemodel',
            name='answer_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='enquetemodel',
            name='delete_flag',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='enquetemodel',
            name='registration_date',
            field=models.DateField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='membermodel',
            name='delete_flag',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='membermodel',
            name='registration_date',
            field=models.DateField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
    ]
