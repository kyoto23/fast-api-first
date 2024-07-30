from typing import List
from fastapi import FastAPI
from models import models2

app = FastAPI(
    title="Trading App"
)

fake_trades = [
    {"id": 1, "user_id": 1, "currency": "BTC", "side": "buy", "price": 123, "amount": 2.12},
    {"id": 2, "user_id": 1, "currency": "BTC", "side": "sell", "price": 113, "amount": 2.24}
]

@app.get("/trades")
def get_trades(limit: int = 1, offset: int = 0):
    return fake_trades[offset:][:limit]

@app.post("/trades")
def add_trades(trades: List[models2.Trade]):
    fake_trades.extend(trades)
    return {"status": 200, "data": fake_trades}

fake_users = [
    {"id": 1, "role": "admin", "name": "popov"},
    {"id": 2, "role": "investor", "name": "vitalya"},
    {"id": 3, "role": "trader", "name": "artem"},
    {"id": 4, "role": "investor", "name": "oleksiy", "degree":[
        {"id": 1, "created_at": "2020-01-01T00:00:00", "type_degree": "expert"}
    ]},
]

@app.get("/users/{user_id}", response_model=List[models2.User])
def get_user(user_id: int):
    return [user for user in fake_users if user.get("id") == user_id]

@app.post("/users/{user_id}")
def change_user_name(user_id: int, new_name: str):
    current_user = list(filter(lambda user: user.get("id") == user_id, fake_users))[0]
    current_user["name"] = new_name
    return {"status": 200, "data": current_user}
