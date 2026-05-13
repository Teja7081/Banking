from django.urls import path

from . import views

urlpatterns = [

    path(
        '',
        views.dashboard,
        name='dashboard'
    ),

    path(
        'signup/',
        views.signup_view,
        name='signup'
    ),

    path(
        'login/',
        views.login_view,
        name='login'
    ),

    path(
        'logout/',
        views.logout_view,
        name='logout'
    ),

    path(
        'profile/',
        views.profile,
        name='profile'
    ),

    path(
        'transfer/',
        views.transfer,
        name='transfer'
    ),

    path(
        'check-balance/',
        views.check_balance,
        name='check_balance'
    ),

    path(
        'transactions/',
        views.transactions,
        name='transactions'
    ),
    path(
        'pay-bill/',
        views.pay_bill,
        name='pay_bill'
    ),
    path(
        'add-card/',
        views.add_card,
        name='add_card'
    ),
    path(
        'cards/',
        views.cards,
        name='cards'
    ),
]