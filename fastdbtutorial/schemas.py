#schemas.py
from typing import Optional
from pydantic import BaseModel
from datetime import datetime,date

class FinanceData(BaseModel):
    status: str
    card_present_flag: str
    bpay_biller_code: str
    account: str
    currency: str
    long_lat: str
    txn_description: str
    merchant_id: str
    merchant_code: float
    first_name: str
    balance: float
    transaction_date: str
    gender: str
    age: int
    merchant_suburb: str
    merchant_state: str
    extraction_timestamp: datetime
    transaction_amount: float
    transaction_id: str
    country: str
    customer_id: str
    merchant_long_lat: str
    movement: str

class Transaction(FinanceData):
    transaction_id: str
    transaction_date: str
    transaction_amount: float

    class Config:
        orm_mode = True
#Pydantic's orm_mode will tell the Pydantic model to read the data #even if it is not a dict, but an ORM model (or any other arbitrary #object with attributes).
