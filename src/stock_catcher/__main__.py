import sys
from pathlib import Path
from catcher import *

def main():
    """Read the stock file and run the stock catcher."""

    # If a stock symbol file path is given, then use give file path
    if len(sys.argv) > 1:
        stock_file_path = Path(sys.argv[1])
    else:
        stock_file_path = get_default_cac_file_path()
    try:
        stock_tickers = get_fr_stock_tickers(stock_file_path)
        stock_info_pdf = get_stock_infos(stock_tickers)
    except FileNotFoundError:
        print(f"The given file path {stock_file_path.as_posix()} not found")
        sys.exit(1)
    print(stock_info_pdf)
    top_div=get_top_dividendYield_stock(stock_info_pdf)
    top_pot = get_top_potential_stock(stock_info_pdf)
    print(f"Top Dividend:\n{top_div}")
    print(f"Top potential:\n{top_pot}")

if __name__ == "__main__":
    main()