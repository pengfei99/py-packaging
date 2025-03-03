from stock_catcher.analyzer import StockAnalyzer


def test_getStockLatestPrice():
    stock_analyzer = StockAnalyzer("ticker1")
    stock_analyzer.get_stock_latest_price("01/01/2021","01/01/2022")
