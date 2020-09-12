from shopping_cart.extras import get_user_pending_order


# so number of items in cart in all views
def cart_context(request):
    if request.user.is_authenticated:
        existing_order = get_user_pending_order(request)
        return {'cart_context': existing_order}
    else:
        return {}