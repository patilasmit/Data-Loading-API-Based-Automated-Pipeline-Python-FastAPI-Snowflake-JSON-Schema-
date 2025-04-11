**⚡ Retail Data Pipeline with FastAPI + Snowflake** 
A real-world Python solution to automate messy CSV uploads into clean, analytics-ready warehouse tables.

**🧠 Problem Statement**
In retail businesses, data analysts and operations teams often receive raw sales data in CSV format from franchises, stores, or partners. 

These files typically contain:
- Inconsistent date formats
- Null or missing values
- Incorrect or mixed data types
- Duplicate records
And they require manual uploads to databases like Snowflake. This process is time-consuming, error-prone, and blocks timely insights for business decision-making.

💡 Why This Matters (Business Challenge)
📉 Reports and dashboards get delayed due to bad data

⚠️ One timestamp error can crash a full BI pipeline

⛔ Analysts waste hours manually cleaning and uploading files

🕵️ Managers can’t make quick decisions without reliable data

**✅Solution**
I designed and built a FastAPI-based Python application that automates this entire process — from raw file to clean data in Snowflake — in under 5 seconds.

🔁 Reusable API to upload any CSV file
🧼 Automated data cleaning using Pandas: date parsing, type conversion, null handling, and duplicate removal
💡 Added calculated fields like PROFIT_MARGIN, ORDER_YEAR, IS_DISCOUNTED
❄️ Seamless integration with Snowflake using the Python connector and secure .env configurations
💥 Error-handling for edge cases like binding errors, timestamps, NaNs


**💥 What Makes This Project Stand Out**
🔧 FastAPI for creating a robust backend API

🧼 Pandas for powerful, scalable data cleaning

❄️ Snowflake integration with error-proof insertion logic

✅ Smart handling of tricky real-world problems (like timestamp binding, nulls, mixed types)

📦 Deployable, testable, and reusable ETL system


**📊 Real-World Use Case**
Imagine you're in a retail team that receives thousands of rows of sales data every day from vendors, franchisees, or internal branches. Instead of cleaning that in Excel manually:

Upload the CSV to /upload-to-snowflake

Get instant cleaning, enrichment, and warehousing

Unlock dashboards, KPIs, and insights with 0 data team delay

🎯 It’s like giving your data superpowers — instantly accessible, trusted, and always clean.
