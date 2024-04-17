# API Financedata

Benvenuto nell'API Financedata! Questa API fornisce accesso a dati finanziari, inclusi dettagli su transazioni, conti e clienti.

## Endpoint Disponibili

### GET /finance_data

Questo endpoint restituisce una lista di dati finanziari.

#### Parametri della Query String

Nessuno.

#### Esempio di Utilizzo

```bash
curl -X GET "http://localhost:8000/finance_data"
```

```json
[
    {
        "status": "authorized",
        "card_present_flag": "1",
        ...
    },
    {
        "status": "authorized",
        "card_present_flag": "0",
        ...
    },
    ...
]
```

## Come Iniziare

1. Clona il repository.
2. Assicurati di avere Python e pip installati sul tuo sistema.
3. Installa le dipendenze con pip install -r requirements.txt.
4. Avvia l'applicazione con uvicorn main:app --reload.
5. Visita http://localhost:8000/docs per interagire con l'API tramite Swagger UI.

## Dipendenze

1. FastAPI
2. Pydantic
3. Uvicorn
4. Poetry

## Licenza

 Questo progetto è distribuito sotto i termini della licenza MIT. Vedi il file `LICENSE` per maggiori informazioni.
