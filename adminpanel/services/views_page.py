from adminpanel.models import Orders, Product


def table_all() -> list:
    """Список заказов и товаров для таблицы отображения"""

    orders = Orders.objects.all()[:50]
    prod = list()

    for item in orders:
        prod.append(Product.objects.filter(number_order=item.number))

    #TODO оптимизировать отображение в шаблоне под этот запрос
    # orders = Orders.objects.all()[:10]
    # orders_number = set(orders.values_list("number", flat=True))
    # prod = Product.objects.filter(number_order__in=orders_number)

    return orders, prod;


def table_article() -> list:
    """Список заказов по артиклу или вхождению оного"""

    orders = Orders.objects.all()[:10]
    orders_number = set(orders.values_list("number", flat=True))
    prod = Product.objects.filter(number_order__in=orders_number)

    return orders, prod;