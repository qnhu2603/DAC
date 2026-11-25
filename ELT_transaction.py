import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

data = pd.read_csv(r'transactions.csv')

#Configure the database connection
DB_USER ='postgres'
DB_PASSWORD = quote_plus("hanhu2603@")
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "postgres"

#Connection string
connection_string = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

#Engine
try: 
    engine = create_engine(connection_string)
    print("Engine created successfully.")
except Exception as e:
    print(f"Error creating engine: {e}")

data.to_sql(
    name='transactions',
    schema='bronze',
    if_exists='replace',
    con=engine
)