from establish_conn import est_conn
from read_csv import read_csv

data = read_csv()
cursor = est_conn()

for each in data[:5]:
    first_data = each
    date = first_data['date']
    symbol = first_data['symbol']
    name = first_data['name']
    high = first_data['high']
    low= first_data['low']

    sql = f"""
    INSERT INTO MYSHARE(DATE,SYMBOL,NAME,HIGH,LOW) VALUES ('{date}','{symbol}','{name}','{high}','{low}')
    """
    print(first_data)


cursor.execute(sql)
print("Details added sucessfully!")