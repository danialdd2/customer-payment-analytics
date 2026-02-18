Customer Payment Analytics
About

This project reads customer payment data from a PostgreSQL database and analyzes it using Python.

It uses Pandas to calculate some basic statistics and SQLAlchemy ORM to save the results into a new table.

I made this project to practice working with databases, Pandas, and SQLAlchemy.

Tools

Python

PostgreSQL

SQLAlchemy

Pandas

Files
database.py   -> database connection
models.py     -> table model
queries.py    -> SQL query
analysis.py   -> data analysis
main.py       -> main file

What it does

For each customer, it calculates:

total payment

number of payments

average payment

customer level (VIP, Regular, Low)

Then it saves the result into a table called:

customer_analytics

Run

Install packages:

pip install sqlalchemy pandas psycopg2


Run:

python main.py

Author

Danial
