# Generated by Django 5.1 on 2024-10-08 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Team_3E_apart', '0004_alter_customuser_groups_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='topic',
            field=models.CharField(choices=[('사는 얘기', '사는 얘기'), ('자랑하기', '자랑하기'), ('친목', '친목'), ('알립니다', '알립니다')], default='사는 얘기', max_length=10),
        ),
    ]