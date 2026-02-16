from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, Float, String


class Base(DeclarativeBase):
    pass


class CustomerAnalytics(Base):
    __tablename__ = "customer_analytics"

    customer_id: Mapped[int] = mapped_column(Integer, primary_key=True)

    total_payment: Mapped[float] = mapped_column(Float)

    number_of_payments: Mapped[int] = mapped_column(Integer)

    average_payment: Mapped[float] = mapped_column(Float)

    customer_level: Mapped[str] = mapped_column(String(20))
