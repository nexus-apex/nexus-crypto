from django.urls import path
from . import views

urlpatterns = [
    path('', lambda r: views.redirect('/dashboard/')),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('portfolios/', views.portfolio_list, name='portfolio_list'),
    path('portfolios/create/', views.portfolio_create, name='portfolio_create'),
    path('portfolios/<int:pk>/edit/', views.portfolio_edit, name='portfolio_edit'),
    path('portfolios/<int:pk>/delete/', views.portfolio_delete, name='portfolio_delete'),
    path('cryptoassets/', views.cryptoasset_list, name='cryptoasset_list'),
    path('cryptoassets/create/', views.cryptoasset_create, name='cryptoasset_create'),
    path('cryptoassets/<int:pk>/edit/', views.cryptoasset_edit, name='cryptoasset_edit'),
    path('cryptoassets/<int:pk>/delete/', views.cryptoasset_delete, name='cryptoasset_delete'),
    path('cryptotransactions/', views.cryptotransaction_list, name='cryptotransaction_list'),
    path('cryptotransactions/create/', views.cryptotransaction_create, name='cryptotransaction_create'),
    path('cryptotransactions/<int:pk>/edit/', views.cryptotransaction_edit, name='cryptotransaction_edit'),
    path('cryptotransactions/<int:pk>/delete/', views.cryptotransaction_delete, name='cryptotransaction_delete'),
    path('settings/', views.settings_view, name='settings'),
    path('api/stats/', views.api_stats, name='api_stats'),
]
