import pandas as pd
class Market(object):

    def __init__(self):
        self.prd_daily = pd.read_csv("2.产品单位净值数据.csv", encoding='gbk', engine='python', error_bad_lines=False)
        self.ben_daily = pd.read_csv("2.指数收盘价.csv", encoding='gbk', engine='python')

        self.prd_daily.TradingDate = self.prd_daily.TradingDate.apply(pd.to_datetime)
        self.ben_daily.TradingDate = self.ben_daily.TradingDate.apply(pd.to_datetime)


class Account(object):

    def __init__(self):
        from collections import deque
        self.prd_position = deque()
        self.ben_position = deque()

    def trackValue(self, end_date, market):

        prd_value, ben_value = 0, 0
        df = market.prd_daily
        df_ben = market.ben_daily

        for shares, start_date in self.prd_position:
            end_price = df[df.TradingDate == end_date].NetValue.values[0]
            prd_value += shares * end_price
        for shares, start_date in self.ben_position:
            ben_end_price = df_ben.iloc[:, 2][df_ben.TradingDate == end_date]
            ben_value += shares * ben_end_price

        return (prd_value, ben_value)

    def buy(self, money, date, market):

        df = market.prd_daily
        prd_shares = money / df[df.TradingDate == date].NetValue.values[0]
        self.prd_position.append((prd_shares, date))

        df = market.ben_daily
        ben_shares = money / df.iloc[:, 2][df.TradingDate == date].values[0]
        self.ben_position.append((ben_shares, date))

    def sell(self, shares, end_date, market):

        df = market.prd_daily
        df_ben = market.ben_daily
        ben_shares = 0  # corresponding bench mark shares to sell
        prd_profit = 0
        while self.prd_position:
            cur_pos, start_date = self.prd_position.popleft()
            if cur_pos <= shares:
                shares -= cur_pos

                # prd_profit
                start_price = df[df.TradingDate == start_date].NetValue.values[0]
                end_price = df[df.TradingDate == end_date].NetValue.values[0]
                prd_profit += cur_pos * (end_price - start_price)

                # ben_profit
                ben_start_price = df_ben.iloc[:, 2][df_ben.TradingDate == start_date]
                ben_shares += cur_pos * start_price / ben_start_price

            else:  # cur_pos > shares
                # prd_profit
                cur_pos -= shares
                start_price = df[df.TradingDate == start_date].NetValue.values[0]
                end_price = df[df.TradingDate == end_date].NetValue.values[0]
                prd_profit += shares * (end_price - start_price)
                self.prd_position.appendleft((cur_pos, start_date))

                # ben_profit
                ben_start_price = df_ben.iloc[:, 2][df_ben.TradingDate == start_date].values[0]
                ben_shares += shares * start_price / ben_start_price
                print (ben_shares)
                break

        ben_profit = 0
        while self.ben_position:
            cur_pos, start_date = self.ben_position.popleft()

            if cur_pos <= ben_shares:
                ben_shares -= cur_pos

                # ben_profit
                ben_start_price = df_ben.iloc[:, 2][df_ben.TradingDate == start_date]
                ben_end_price = df_ben.iloc[:, 2][df_ben.TradingDate == end_date]
                ben_profit += cur_pos * (ben_end_price - ben_start_price)

            else:  # cur_pos > shares
                # prd_profit
                cur_pos -= ben_shares
                ben_start_price = df_ben.iloc[:, 2][df_ben.TradingDate == start_date]
                ben_end_price = df_ben.iloc[:, 2][df_ben.TradingDate == end_date]
                ben_profit += shares * (ben_end_price - ben_start_price)
                self.ben_position.appendleft((cur_pos, start_date))

                break

        return (prd_profit, ben_profit)


if __name__ == "__main__":
    market = Market()
    acct = Account()
    df_position = pd.read_csv("2.产品申赎数据.csv", encoding='gbk', engine='python', error_bad_lines=False)
    df_position.confirmDate = df_position.confirmDate.apply(pd.to_datetime)
    for index, row in df_position.iterrows():
        if row.tag == '申购':
            acct.buy(row.applyMoney, row.confirmDate, market)

        elif row.tag == '赎回':
            acct.sell(row.applyShares, row.confirmDate, market)

    print(acct.ben_position, acct.prd_position)