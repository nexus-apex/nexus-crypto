import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Sum, Count
from .models import Portfolio, CryptoAsset, CryptoTransaction


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/dashboard/')
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/dashboard/')
        error = 'Invalid credentials. Try admin / Admin@2024'
    return render(request, 'login.html', {'error': error})


def logout_view(request):
    logout(request)
    return redirect('/login/')


@login_required
def dashboard_view(request):
    ctx = {}
    ctx['portfolio_count'] = Portfolio.objects.count()
    ctx['portfolio_active'] = Portfolio.objects.filter(status='active').count()
    ctx['portfolio_archived'] = Portfolio.objects.filter(status='archived').count()
    ctx['portfolio_total_total_value'] = Portfolio.objects.aggregate(t=Sum('total_value'))['t'] or 0
    ctx['cryptoasset_count'] = CryptoAsset.objects.count()
    ctx['cryptoasset_binance'] = CryptoAsset.objects.filter(exchange='binance').count()
    ctx['cryptoasset_coinbase'] = CryptoAsset.objects.filter(exchange='coinbase').count()
    ctx['cryptoasset_wazirx'] = CryptoAsset.objects.filter(exchange='wazirx').count()
    ctx['cryptoasset_total_quantity'] = CryptoAsset.objects.aggregate(t=Sum('quantity'))['t'] or 0
    ctx['cryptotransaction_count'] = CryptoTransaction.objects.count()
    ctx['cryptotransaction_buy'] = CryptoTransaction.objects.filter(transaction_type='buy').count()
    ctx['cryptotransaction_sell'] = CryptoTransaction.objects.filter(transaction_type='sell').count()
    ctx['cryptotransaction_transfer'] = CryptoTransaction.objects.filter(transaction_type='transfer').count()
    ctx['cryptotransaction_total_quantity'] = CryptoTransaction.objects.aggregate(t=Sum('quantity'))['t'] or 0
    ctx['recent'] = Portfolio.objects.all()[:10]
    return render(request, 'dashboard.html', ctx)


@login_required
def portfolio_list(request):
    qs = Portfolio.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(name__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(status=status_filter)
    return render(request, 'portfolio_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def portfolio_create(request):
    if request.method == 'POST':
        obj = Portfolio()
        obj.name = request.POST.get('name', '')
        obj.owner = request.POST.get('owner', '')
        obj.total_value = request.POST.get('total_value') or 0
        obj.total_invested = request.POST.get('total_invested') or 0
        obj.pnl = request.POST.get('pnl') or 0
        obj.assets_count = request.POST.get('assets_count') or 0
        obj.status = request.POST.get('status', '')
        obj.created_date = request.POST.get('created_date') or None
        obj.currency = request.POST.get('currency', '')
        obj.save()
        return redirect('/portfolios/')
    return render(request, 'portfolio_form.html', {'editing': False})


@login_required
def portfolio_edit(request, pk):
    obj = get_object_or_404(Portfolio, pk=pk)
    if request.method == 'POST':
        obj.name = request.POST.get('name', '')
        obj.owner = request.POST.get('owner', '')
        obj.total_value = request.POST.get('total_value') or 0
        obj.total_invested = request.POST.get('total_invested') or 0
        obj.pnl = request.POST.get('pnl') or 0
        obj.assets_count = request.POST.get('assets_count') or 0
        obj.status = request.POST.get('status', '')
        obj.created_date = request.POST.get('created_date') or None
        obj.currency = request.POST.get('currency', '')
        obj.save()
        return redirect('/portfolios/')
    return render(request, 'portfolio_form.html', {'record': obj, 'editing': True})


@login_required
def portfolio_delete(request, pk):
    obj = get_object_or_404(Portfolio, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/portfolios/')


@login_required
def cryptoasset_list(request):
    qs = CryptoAsset.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(name__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(exchange=status_filter)
    return render(request, 'cryptoasset_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def cryptoasset_create(request):
    if request.method == 'POST':
        obj = CryptoAsset()
        obj.name = request.POST.get('name', '')
        obj.symbol = request.POST.get('symbol', '')
        obj.portfolio_name = request.POST.get('portfolio_name', '')
        obj.quantity = request.POST.get('quantity') or 0
        obj.avg_buy_price = request.POST.get('avg_buy_price') or 0
        obj.current_price = request.POST.get('current_price') or 0
        obj.value = request.POST.get('value') or 0
        obj.pnl_percent = request.POST.get('pnl_percent') or 0
        obj.exchange = request.POST.get('exchange', '')
        obj.save()
        return redirect('/cryptoassets/')
    return render(request, 'cryptoasset_form.html', {'editing': False})


@login_required
def cryptoasset_edit(request, pk):
    obj = get_object_or_404(CryptoAsset, pk=pk)
    if request.method == 'POST':
        obj.name = request.POST.get('name', '')
        obj.symbol = request.POST.get('symbol', '')
        obj.portfolio_name = request.POST.get('portfolio_name', '')
        obj.quantity = request.POST.get('quantity') or 0
        obj.avg_buy_price = request.POST.get('avg_buy_price') or 0
        obj.current_price = request.POST.get('current_price') or 0
        obj.value = request.POST.get('value') or 0
        obj.pnl_percent = request.POST.get('pnl_percent') or 0
        obj.exchange = request.POST.get('exchange', '')
        obj.save()
        return redirect('/cryptoassets/')
    return render(request, 'cryptoasset_form.html', {'record': obj, 'editing': True})


@login_required
def cryptoasset_delete(request, pk):
    obj = get_object_or_404(CryptoAsset, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/cryptoassets/')


@login_required
def cryptotransaction_list(request):
    qs = CryptoTransaction.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(asset_name__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(transaction_type=status_filter)
    return render(request, 'cryptotransaction_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def cryptotransaction_create(request):
    if request.method == 'POST':
        obj = CryptoTransaction()
        obj.asset_name = request.POST.get('asset_name', '')
        obj.transaction_type = request.POST.get('transaction_type', '')
        obj.quantity = request.POST.get('quantity') or 0
        obj.price = request.POST.get('price') or 0
        obj.total = request.POST.get('total') or 0
        obj.fee = request.POST.get('fee') or 0
        obj.date = request.POST.get('date') or None
        obj.exchange = request.POST.get('exchange', '')
        obj.notes = request.POST.get('notes', '')
        obj.save()
        return redirect('/cryptotransactions/')
    return render(request, 'cryptotransaction_form.html', {'editing': False})


@login_required
def cryptotransaction_edit(request, pk):
    obj = get_object_or_404(CryptoTransaction, pk=pk)
    if request.method == 'POST':
        obj.asset_name = request.POST.get('asset_name', '')
        obj.transaction_type = request.POST.get('transaction_type', '')
        obj.quantity = request.POST.get('quantity') or 0
        obj.price = request.POST.get('price') or 0
        obj.total = request.POST.get('total') or 0
        obj.fee = request.POST.get('fee') or 0
        obj.date = request.POST.get('date') or None
        obj.exchange = request.POST.get('exchange', '')
        obj.notes = request.POST.get('notes', '')
        obj.save()
        return redirect('/cryptotransactions/')
    return render(request, 'cryptotransaction_form.html', {'record': obj, 'editing': True})


@login_required
def cryptotransaction_delete(request, pk):
    obj = get_object_or_404(CryptoTransaction, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/cryptotransactions/')


@login_required
def settings_view(request):
    return render(request, 'settings.html')


@login_required
def api_stats(request):
    data = {}
    data['portfolio_count'] = Portfolio.objects.count()
    data['cryptoasset_count'] = CryptoAsset.objects.count()
    data['cryptotransaction_count'] = CryptoTransaction.objects.count()
    return JsonResponse(data)
