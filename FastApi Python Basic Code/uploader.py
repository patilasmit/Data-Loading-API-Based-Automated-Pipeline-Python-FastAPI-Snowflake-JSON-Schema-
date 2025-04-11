import snowflake.connector
import os
from dotenv import load_dotenv
import pandas as pd  # ✅ Needed for Timestamp check

load_dotenv()

def upload_to_snowflake(df, table_name="Retail"):
    conn = snowflake.connector.connect(
        user=os.getenv("SNOWFLAKE_USER"),
        password=os.getenv("SNOWFLAKE_PASSWORD"),
        account=os.getenv("SNOWFLAKE_ACCOUNT"),
        warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
        database=os.getenv("SNOWFLAKE_DATABASE"),
        schema=os.getenv("SNOWFLAKE_SCHEMA")
    )
    cursor = conn.cursor()

    # ✅ Use IF NOT EXISTS to prevent failure if table exists
    create_table_query = f"""
    CREATE TABLE IF NOT EXISTS Retail (
        ROW_ID INT,
        ORDER_ID VARCHAR,
        ORDER_DATE DATE,
        SHIP_DATE DATE,
        SHIP_MODE VARCHAR,
        CUSTOMER_ID VARCHAR,
        CUSTOMER_NAME VARCHAR,
        SEGMENT VARCHAR,
        COUNTRY VARCHAR,
        CITY VARCHAR,
        STATE VARCHAR,
        POSTAL_CODE INT,
        REGION VARCHAR,
        PRODUCT_ID VARCHAR,
        CATEGORY VARCHAR,
        SUB_CATEGORY VARCHAR,
        PRODUCT_NAME VARCHAR,
        SALES FLOAT,
        QUANTITY INT,
        DISCOUNT FLOAT,
        PROFIT FLOAT
    );
    """
    cursor.execute(create_table_query)
    

    conn.commit()
    cursor.close()
    conn.close()
