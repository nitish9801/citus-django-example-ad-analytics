# Generated by Django 2.1.7 on 2019-08-21 23:03

from django.db import migrations
import django.db.models.deletion
import django_multitenant.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ad_analytics', '0013_migration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads',
            name='campaign',
            field=django_multitenant.fields.TenantForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ads', to='ad_analytics.Campaign'),
        ),
        migrations.AlterField(
            model_name='campaigncollaborators',
            name='campaign',
            field=django_multitenant.fields.TenantForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ad_analytics.Campaign'),
        ),
        migrations.AlterField(
            model_name='campaigncollaborators',
            name='employee',
            field=django_multitenant.fields.TenantForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ad_analytics.Employee'),
        ),
        migrations.AlterField(
            model_name='click',
            name='ads',
            field=django_multitenant.fields.TenantForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clicks', to='ad_analytics.Ads'),
        ),
        migrations.AlterField(
            model_name='impression',
            name='ads',
            field=django_multitenant.fields.TenantForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='impressions', to='ad_analytics.Ads'),
        ),
    ]
