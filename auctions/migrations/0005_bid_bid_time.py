# Generated by Django 4.2.7 on 2023-12-23 20:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("auctions", "0004_auctionlisting_created_at_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="bid",
            name="bid_time",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]