from django import template
from ..models import ItemShop, Carts

register = template.Library()


@register.inclusion_tag('shop/item.html')
def items_list():
    items = ItemShop.objects.all()
    return {"items": items}


@register.inclusion_tag('shop/cart.html')
def cart_list():
    cart = Carts.objects.all()
    total = 0
    for c in cart:
        total = total + c.summary
    return {"cart": cart, "total": total}
