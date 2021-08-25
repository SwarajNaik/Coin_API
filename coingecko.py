import pandas as pd
from pycoingecko import CoinGeckoAPI

def get_events():
    cg = CoinGeckoAPI()
    enevts = cg.get_events()
    list_ofevents = enevts['data']

    df = pd.DataFrame.from_dict(list_ofevents)
    print(df)
    df.to_csv ('list_of_events.csv', index = False, header=True)

def get_event_country():
    cg = CoinGeckoAPI()
    country = cg.get_events_countries()
    country_ = country['data']
    df = pd.DataFrame.from_dict(country_)
    print(df)

def get_event_type():
    cg =  CoinGeckoAPI()
    type_ = cg.get_events_types()
    type_list = type_['data']
    df = pd.DataFrame.from_dict(type_list)
    print(df)

def get_coin_list():
    cg = CoinGeckoAPI()
    list_ = cg.get_coins_list()
    df = pd.DataFrame.from_dict(list_)
    df.to_csv ('list_of_coins.csv', index = False, header=True)

def current_data():
    cg = CoinGeckoAPI()
    coin = cg.get_coin_by_id('celo')
    return coin



if __name__=="__main__":

    celo_coin = current_data()
    print(celo_coin)
    # df = pd.DataFrame.from_dict(celo_coin)

    