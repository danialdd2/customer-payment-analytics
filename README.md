# Customer Payment Analytics

## Overview

This project analyzes customer payment data from a PostgreSQL database using Python, SQLAlchemy, and Pandas.

The main goal was to practice working with databases, writing SQL queries, processing data with Pandas, and storing the results back into a new table.

This project simulates a simple real-world data analytics workflow.

---

## Tools and Technologies

* Python
* SQLAlchemy
* Pandas
* PostgreSQL
* Git & GitHub

---

## Project Structure

```
customer-payment-analytics/

database.py     -> database connection
models.py      -> table definitions
queries.py     -> SQL query used to extract data
analysis.py    -> data processing and analytics
main.py        -> runs the full pipeline
README.md
```

---

## What the project does

• Connects to a PostgreSQL database
• Extracts customer and payment data using SQL
• Processes the data using Pandas
• Calculates:

* total payment per customer
* number of payments
* average payment
* customer level based on total spending

• Saves the results into a new table called:

```
customer_analytics
```

---

## Example output

Each customer gets analyzed and classified:

* VIP
* Regular
* Low

based on their total payments.

---

## Why I built this project

I created this project to practice:

* working with real databases
* combining SQLAlchemy and Pandas
* building a simple data analysis pipeline
* preparing for data analyst / applied AI roles

---

## How to run

Install requirements:

```
pip install sqlalchemy pandas psycopg2
```

Run the project:

```
python main.py
```

---

## Author

Danial
