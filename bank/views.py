from django.shortcuts import render, redirect

from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth import login, logout

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

from .forms import SignupForm

from .models import Account, Transaction

import random


def signup_view(request):

    form = SignupForm(request.POST or None)

    if form.is_valid():

        user = form.save()

        Account.objects.create(

            user=user,

            balance=1000,

            account_number=str(
                random.randint(
                    10000000000000,
                    99999999999999
                )
            ),

            upi_id=f"{user.username}@safebank",

            card_number=str(
                random.randint(
                    1000000000000000,
                    9999999999999999
                )
            ),

            cvv=str(
                random.randint(
                    100,
                    999
                )
            ),

            expiry_date="12/30",

            ifsc_code="SAFE0001234"
        )

        login(request, user)

        return redirect('dashboard')

    return render(request, 'signup.html', {
        'form': form
    })


def login_view(request):

    form = AuthenticationForm(
        data=request.POST or None
    )

    if form.is_valid():

        login(request, form.get_user())

        return redirect('dashboard')

    return render(request, 'login.html', {
        'form': form
    })


def logout_view(request):

    logout(request)

    return redirect('login')


@login_required
def dashboard(request):

    account = Account.objects.get(
        user=request.user
    )

    transactions = Transaction.objects.filter(
        user=request.user
    ).order_by('-created_at')[:5]

    return render(request, 'dashboard.html', {
        'account': account,
        'transactions': transactions
    })


@login_required
def profile(request):

    account = Account.objects.get(
        user=request.user
    )

    return render(request, 'profile.html', {
        'account': account
    })


@login_required
def check_balance(request):

    account = Account.objects.get(
        user=request.user
    )

    return render(request, 'check_balance.html', {
        'account': account
    })


@login_required
def transfer(request):

    message = ''

    if request.method == 'POST':

        username = request.POST['username']

        amount = int(request.POST['amount'])

        payment_method = request.POST['payment_method']

        sender_account = Account.objects.get(
            user=request.user
        )

        try:

            receiver = User.objects.get(
                username=username
            )

            receiver_account = Account.objects.get(
                user=receiver
            )

            if sender_account.balance >= amount:

                sender_account.balance -= amount
                sender_account.save()

                receiver_account.balance += amount
                receiver_account.save()

                Transaction.objects.create(
                    user=request.user,
                    transaction_type=f'{payment_method} Sent',
                    amount=amount
                )

                Transaction.objects.create(
                    user=receiver,
                    transaction_type=f'{payment_method} Received',
                    amount=amount
                )

                message = 'Transfer Successful'

            else:

                message = 'Insufficient Balance'

        except:

            message = 'User Not Found'

    return render(request, 'transfer.html', {
        'message': message
    })


@login_required
def transactions(request):

    transactions = Transaction.objects.filter(
        user=request.user
    ).order_by('-created_at')

    return render(request, 'transactions.html', {
        'transactions': transactions
    })