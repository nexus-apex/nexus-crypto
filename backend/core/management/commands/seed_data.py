from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import Portfolio, CryptoAsset, CryptoTransaction
from datetime import date, timedelta
import random


class Command(BaseCommand):
    help = 'Seed NexusCrypto with demo data'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@nexuscrypto.com', 'Admin@2024')
            self.stdout.write(self.style.SUCCESS('Admin user created'))

        if Portfolio.objects.count() == 0:
            for i in range(10):
                Portfolio.objects.create(
                    name=f"Sample Portfolio {i+1}",
                    owner=f"Sample {i+1}",
                    total_value=round(random.uniform(1000, 50000), 2),
                    total_invested=round(random.uniform(1000, 50000), 2),
                    pnl=round(random.uniform(1000, 50000), 2),
                    assets_count=random.randint(1, 100),
                    status=random.choice(["active", "archived"]),
                    created_date=date.today() - timedelta(days=random.randint(0, 90)),
                    currency=random.choice(["usd", "inr", "eur"]),
                )
            self.stdout.write(self.style.SUCCESS('10 Portfolio records created'))

        if CryptoAsset.objects.count() == 0:
            for i in range(10):
                CryptoAsset.objects.create(
                    name=f"Sample CryptoAsset {i+1}",
                    symbol=f"Sample {i+1}",
                    portfolio_name=f"Sample CryptoAsset {i+1}",
                    quantity=round(random.uniform(1000, 50000), 2),
                    avg_buy_price=round(random.uniform(1000, 50000), 2),
                    current_price=round(random.uniform(1000, 50000), 2),
                    value=round(random.uniform(1000, 50000), 2),
                    pnl_percent=round(random.uniform(1000, 50000), 2),
                    exchange=random.choice(["binance", "coinbase", "wazirx", "kraken"]),
                )
            self.stdout.write(self.style.SUCCESS('10 CryptoAsset records created'))

        if CryptoTransaction.objects.count() == 0:
            for i in range(10):
                CryptoTransaction.objects.create(
                    asset_name=f"Sample CryptoTransaction {i+1}",
                    transaction_type=random.choice(["buy", "sell", "transfer", "swap"]),
                    quantity=round(random.uniform(1000, 50000), 2),
                    price=round(random.uniform(1000, 50000), 2),
                    total=round(random.uniform(1000, 50000), 2),
                    fee=round(random.uniform(1000, 50000), 2),
                    date=date.today() - timedelta(days=random.randint(0, 90)),
                    exchange=f"Sample {i+1}",
                    notes=f"Sample notes for record {i+1}",
                )
            self.stdout.write(self.style.SUCCESS('10 CryptoTransaction records created'))
