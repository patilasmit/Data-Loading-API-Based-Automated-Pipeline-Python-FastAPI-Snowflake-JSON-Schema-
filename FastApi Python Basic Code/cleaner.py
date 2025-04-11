import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    df.dropna(how='all', inplace=True)
    df.drop_duplicates(inplace=True)

    str_cols = df.select_dtypes(include='object').columns
    df[str_cols] = df[str_cols].apply(lambda x: x.str.strip())

    df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
    df['ship_date'] = pd.to_datetime(df['ship_date'], errors='coerce')
    df['sales'] = pd.to_numeric(df['sales'], errors='coerce').fillna(0.0)
    df['profit'] = pd.to_numeric(df['profit'], errors='coerce').fillna(0.0)
    df['discount'] = pd.to_numeric(df['discount'], errors='coerce').fillna(0.0)
    df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce').fillna(0).astype(int)
    df['postal_code'] = pd.to_numeric(df['postal_code'], errors='coerce').fillna(0).astype(int)
    

    df.columns = df.columns.str.upper()
    return df
