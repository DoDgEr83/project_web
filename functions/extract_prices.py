import pandas as pd
import yfinance as yf


def get_prices(ticker: str):
    # msft = yf.Ticker("MSFT")
    msft = yf.Ticker(ticker)

    # get all stock info
    # print(msft.info)

    # get historical market data
    hist = msft.history(period="1mo")
    # print(hist.head(), type(hist))
    hist.reset_index(inplace=True)
    hist["Date"] = hist["Date"].apply(lambda x: x.strftime('%Y-%m-%d'))
    hist.set_index("Date", inplace=True)
    # print(hist)
    return hist[['Close']].reset_index().to_dict('records')

    # # show meta information about the history (requires history() to be called first)
    # print(msft.history_metadata)
    #
    # # show actions (dividends, splits, capital gains)
    # print(msft.actions)
    # print(msft.dividends)
    # print(msft.splits)
    # print(msft.capital_gains)  # only for mutual funds & etfs
    #
    # # show share count
    # print(msft.get_shares_full(start="2022-01-01", end=None))


if __name__ == '__main__':
    print(get_prices('msft'))
