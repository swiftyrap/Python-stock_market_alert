import datetime
import pandas as pd
from pandas_datareader import data

hsbc = '1333.hk'
start_date = '2018-01-01'
end_date = datetime.datetime.today().strftime('%Y-%m-%d')

print(data.get_data_yahoo(hsbc,start=start_date,end=end_date))
