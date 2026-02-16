import pandas as pd
from database import engine
from queries import query


def run_analysis():
    df = pd.read_sql(query, engine)

    df_analytics = df.groupby('customer_id').agg(
        total_payment=('amount', 'sum'),
        payment_counts=('amount', 'count'),
        average_payment=('amount', 'mean')
    ).reset_index()

    df_analytics['customer_level'] = df_analytics['total_payment'].apply(
        lambda x: 'vip' if x > 1000 else ('regular' if x > 500 else 'low')
    )

    return df_analytics
