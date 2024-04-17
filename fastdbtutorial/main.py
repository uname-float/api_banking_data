import crud, models,schemas

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal,engine
from typing import List

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

#Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {"message": "Welcome to the Tutorial Events API!"}

@app.get("/finance-data",response_model=list[schemas.FinanceData])
def read_financedata(skip: int=0, limit: int=1000, db: Session = Depends(get_db)):
    finance_data = crud.get_financedata(db,skip=skip,limit=limit)
    return finance_data

@app.get("/transactions", response_model=List[schemas.Transaction])
async def get_transactions():
    transactions = [Transaction(**item) for item in transaction_data]
    return transactions

@app.get("/transaction/{transaction_id}", response_model=Transaction)
async def get_transaction(transaction_id: str):
    for item in transaction_data:
        if item["transaction_id"] == transaction_id:
            return Transaction(**item)
    return {"message": "Transaction not found"}

if __name__ == "__main__":
     import uvicorn
     uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
