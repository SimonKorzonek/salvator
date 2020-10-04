from django.shortcuts import get_object_or_404
from shopping_cart.models import Order
from users.models import Account
import random
import string
import datetime


def get_user_pending_order(request):
    user_account = get_object_or_404(Account, user=request.user)
    order = Order.objects.filter(owner=user_account, is_ordered=False)
    if order.exists():
        return order[0]
    return 0

def generate_order_id():
    date = datetime.date.today().strftime('%Y%m%d')[2:] + str(datetime.datetime.now().second)
    random_string = "".join([random.choice(string.digits) for rand in range(3)])
    return date + random_string
