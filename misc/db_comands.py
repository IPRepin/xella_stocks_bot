from asgiref.sync import sync_to_async

from admin_panel.stocks_manage.models import Stock


@sync_to_async()
def get_all_stocks():
    stocks = Stock.objects.all()
    return stocks


@sync_to_async()
def get_stock(stock_id: int):
    stock = Stock.objects.filter(id=stock_id).first()
    return stock


@sync_to_async()
def count_stocks():
    return len(Stock.objects.all())