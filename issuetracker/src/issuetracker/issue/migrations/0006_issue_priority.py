# Generated by Django 2.2.3 on 2019-07-31 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('issue', '0005_issue_issuetype'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='priority',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='issue_priority', to='issue.IssuePriority'),
        ),
    ]
