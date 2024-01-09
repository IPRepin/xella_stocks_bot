from misc.db_comands import get_all_stocks


async def sort_promotion(stock_category: str) -> list:
    all_stocks = await get_all_stocks()
    sorted_stocks = []
    for stock in all_stocks:
        if stock_category == "A":
            if stock.category == "B":
                sorted_stocks.append(stock.name_stock)
        elif stock_category == "B":
            if stock.category == "A":
                sorted_stocks.append(stock.name_stock)
    return sorted_stocks
