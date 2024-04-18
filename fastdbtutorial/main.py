import crud, models,schemas

from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

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
    finance_data = jsonable_encoder(crud.get_financedata(db,skip=skip,limit=limit))
    return JSONResponse(content=finance_data)

@app.get("/transactions", response_model=List[schemas.Transaction])
async def get_transactions(db: Session = Depends(get_db)):
    # Ottieni transazioni dal database utilizzando SQLAlchemy
    transactions_from_db = crud.get_financedata(db)

    # Trasforma le transazioni nel formato desiderato
    transactions = [
        schemas.Transaction(
            transaction_id=item.transaction_id,
            transaction_date=item.transaction_date,
            transaction_amount=item.transaction_amount
        ) for item in transactions_from_db
    ]
    print(transactions)
    # Utilizza jsonable_encoder per convertire gli oggetti Pydantic in JSON
    transactions_json = jsonable_encoder(transactions)

    # Restituisci i dati come JSONResponse
    return JSONResponse(content=transactions_json)

    #transactions = [Transaction(**item) for item in transaction_data]
    #return transactions

@app.get("/transaction/{transaction_id}", response_model=schemas.Transaction)
async def get_transaction(transaction_id: str, db: Session = Depends(get_db)):
    # Ottieni transazioni dal database utilizzando SQLAlchemy
    transactions_from_db = crud.get_financedata(db)

    for item in jsonable_encoder(transactions_from_db):
        if item["transaction_id"] == transaction_id:
            return JSONResponse(cont