from django.db import models

class Portfolio(models.Model):
    name = models.CharField(max_length=255)
    owner = models.CharField(max_length=255, blank=True, default="")
    total_value = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total_invested = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    pnl = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    assets_count = models.IntegerField(default=0)
    status = models.CharField(max_length=50, choices=[("active", "Active"), ("archived", "Archived")], default="active")
    created_date = models.DateField(null=True, blank=True)
    currency = models.CharField(max_length=50, choices=[("usd", "USD"), ("inr", "INR"), ("eur", "EUR")], default="usd")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

class CryptoAsset(models.Model):
    name = models.CharField(max_length=255)
    symbol = models.CharField(max_length=255, blank=True, default="")
    portfolio_name = models.CharField(max_length=255, blank=True, default="")
    quantity = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    avg_buy_price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    current_price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    value = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    pnl_percent = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    exchange = models.CharField(max_length=50, choices=[("binance", "Binance"), ("coinbase", "Coinbase"), ("wazirx", "WazirX"), ("kraken", "Kraken")], default="binance")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

class CryptoTransaction(models.Model):
    asset_name = models.CharField(max_length=255)
    transaction_type = models.CharField(max_length=50, choices=[("buy", "Buy"), ("sell", "Sell"), ("transfer", "Transfer"), ("swap", "Swap")], default="buy")
    quantity = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    fee = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    date = models.DateField(null=True, blank=True)
    exchange = models.CharField(max_length=255, blank=True, default="")
    notes = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.asset_name
