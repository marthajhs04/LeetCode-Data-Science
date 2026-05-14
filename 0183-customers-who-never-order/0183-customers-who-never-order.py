import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    tabla_unida = customers.merge(orders, left_on='id', right_on='customerId', how='left')

    clientes_sin_compras = tabla_unida[tabla_unida['customerId'].isna()]

    return clientes_sin_compras[['name']].rename(columns={'name': 'Customers'})