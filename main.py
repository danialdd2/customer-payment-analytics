from database import engine
from models import Base, CustomerAnalytics
from analysis import run_analysis
from database import SessionLocal
Base.metadata.create_all(engine)

result_df = run_analysis()

session = SessionLocal()

for _, i in result_df.iterrows():
    customer = CustomerAnalytics(
        customer_id=i['customer_id'],
        total_payment=i['total_payment'],
        number_of_payments=i['payment_counts'],
        average_payment=i['average_payment'],
        customer_level=i['customer_level']
    )
    session.add(customer)
session.commit()
session.close()
