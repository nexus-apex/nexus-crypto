from django.contrib import admin
from .models import Portfolio, CryptoAsset, CryptoTransaction

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ["name", "owner", "total_value", "total_invested", "pnl", "created_at"]
    list_filter = ["status", "currency"]
    search_fields = ["name", "owner"]

@admin.register(CryptoAsset)
class CryptoAssetAdmin(admin.ModelAdmin):
    list_display = ["name", "symbol", "portfolio_name", "quantity", "avg_buy_price", "created_at"]
    list_filter = ["exchange"]
    search_fields = ["name", "symbol", "portfolio_name"]

@admin.register(CryptoTransaction)
class CryptoTransactionAdmin(admin.ModelAdmin):
    list_display = ["asset_name", "transaction_type", "quantity", "price", "total", "created_at"]
    list_filter = ["transaction_type"]
    search_fields = ["asset_name", "exchange"]
