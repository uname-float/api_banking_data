#models.py
from sqlalchemy import Boolean, Column, Integer, String, Date, DateTime,Float,Text
from database import Base
#The __tablename__ attribute should be the actual name of the #database we are connecting to
class FinanceData(Base):
    __tablename__ = "financial_data"

    status = Column(Text)
    card_present_flag = Column(Text)
    bpay_biller_code = Column(Text)
    account = Column(Text)
    currency = Column(Text)
    long_lat = Column(Text)
    txn_description = Column(Text)
    merchant_id = Column(Text)
    merchant_code = Column(Float)
    first_name = Column(Text)
    balance = Column(Float)
    transaction_date = Column(Date)
    gender = Column(Text)
    age = Column(Integer)
    merchant_suburb = Column(Text)
    merchant_state = Column(Text)
    extraction_timestamp = Column(DateTime)
    transaction_amount = Column(Float)
    transaction_id = Column(Text,primary_key=True)
    country = Column(Text)
    customer_id = Column(Text)
    merchant_long_lat = Column(Text)
    movement = Column(Text)
