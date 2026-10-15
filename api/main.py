from pydantic import BaseModel
import fastapi
from api.db import get_connection

class Score(BaseModel):
    username: str
    score: float
    level: int

scores = []       # pagaidām saraksts atmiņā

app = fastapi.FastAPI()

@app.post("/scores", status_code=201)
def add_score(item: Score):
    with get_connection() as conn:
        conn.execute(
            "INSERT INTO scores (username, score, level) VALUES (?, ?, ?)",
            (item.username, item.score, item.level))
    return item

@app.get("/scores/top")
def top():
    with get_connection() as conn:
        rows = conn.execute(
            "SELECT username, score, level FROM scores "
            "ORDER BY score DESC LIMIT 10").fetchall()
    return [{"username": p, "score": s, "level": l} for p, s, l in rows]
