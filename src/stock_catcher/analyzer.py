"""
This module provides a class to analyze stock prices.

"""
import pandas as pd


class StockAnalyzer:
    """
    Represents a stock analyzer in the system.

    :param stock_ticker: The stock's unique identifier
    :type stock_ticker: str


    :ivar stock_ticker: The stock's unique identifier
    :vartype stock_ticker: str

    """

    ALLOW_TICKERS = ["ticker1", "ticker2"]

    def __init__(self, stock_ticker:str):
        """
        Initializes a stock analyzer instance.
        :param stock_ticker: The stock's unique identifier
        :type stock_ticker: str
        """
        self.stock_ticker = stock_ticker

    def get_stock_latest_price(self,start_date:str,end_date:str)->pd.DataFrame:
        """
        This function takes a stock ticker and returns a Pandas DataFrame which contains the latest price of the stock
        within the given date range.
        :param start_date: start date
        :type start_date: str
        :param end_date: end date
        :type end_date: str
        :return: a pandas dataframe containing the latest price of the stock
        :rtype: pd.DataFrame
        :raise ValueError: if stock ticker does not exist

        :Example:

        . code-block:: python
           stock_analyzer = StockAnalyzer("ticker1")
           stock_analyzer.get_stock_latest_price(start_date="2020-01-01",end_date="2020-02-25")
        """
        result = pd.DataFrame()
        if self.stock_ticker not in StockAnalyzer.ALLOW_TICKERS:
            raise ValueError(f"The stock ticker {self.stock_ticker} is no longer valid.")
        print(f"Getting latest price for stock ticker: {self.stock_ticker} with start date: {start_date} and end date: {end_date}")
        return result
