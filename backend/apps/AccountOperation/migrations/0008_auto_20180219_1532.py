# Generated by Django 2.0.2 on 2018-02-19 15:32

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Question', '0008_auto_20180218_1742'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AccountOperation', '0007_auto_20180218_1755'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserFav',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fav', to='Question.Answer', verbose_name='回答')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fav', to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '用户收藏问题',
                'verbose_name_plural': '用户收藏问题',
            },
        ),
        migrations.AlterUniqueTogether(
            name='userfav',
            unique_together={('user', 'answer')},
        ),
    ]
