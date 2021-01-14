# Generated by Django 3.1 on 2020-09-03 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MaskCCTV', '0005_auto_20200903_1622'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='maskinfo',
            options={'ordering': ['adress']},
        ),
        migrations.AlterField(
            model_name='maskinfo',
            name='adress',
            field=models.CharField(choices=[('namchuncheon', '강원도 춘천시 효자동 남춘천역'), ('gangnam', '서울시 강남구 강남역'), ('sareung', '경기도 남양주시 사릉역')], default='namchuncheon', help_text='CCTV 주소', max_length=20),
        ),
    ]