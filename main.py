from database import engine
from models import Base, CustomerAnalytics
from analysis import run_analysis

Base.metadata.create_all(engine)

result_df = run_analysis()


result_df.to_sql(
    "customer_analytics",
    engine,
    if_exists="replace",
    index=False
)

print("done. Tavle customer_analytics created.")
