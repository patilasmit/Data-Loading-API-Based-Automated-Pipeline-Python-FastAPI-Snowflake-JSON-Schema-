from fastapi import FastAPI, UploadFile, File, HTTPException
from etl.cleaner import clean_data
from etl.uploader import upload_to_snowflake
import pandas as pd
import io
import os
import logging

app = FastAPI(title="Retail Sales ETL API")

logging.basicConfig(level=logging.INFO)

@app.post("/clean-data")
async def clean_uploaded_data(file: UploadFile = File(...)):
    try:
        df = pd.read_csv(io.BytesIO(await file.read()), encoding='latin1')
        cleaned_df = clean_data(df)
        return cleaned_df.head(10).to_dict(orient="records")
    except Exception as e:
        logging.error(f"Cleaning error: {e}")
        raise HTTPException(status_code=500, detail="Cleaning failed")

@app.post("/upload-to-snowflake")
async def upload_data_to_snowflake(file: UploadFile = File(...)):
    try:
        df = pd.read_csv(io.BytesIO(await file.read()), encoding='latin1')
        cleaned_df = clean_data(df)
        upload_to_snowflake(cleaned_df, table_name="Retail")
        return {
            "message": "Data uploaded to Snowflake successfully",
            "database": os.getenv("SNOWFL"),
            "schema": os.getenv("SNOWFLAKE_SCHEMA"),
            "table": "SALES_SUPERSTORE"
        }
    except Exception as e:
        logging.error(f"Upload error: {e}")
        raise HTTPException(status_code=500, detail=str(e))
