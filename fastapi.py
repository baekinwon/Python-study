from fastapi import FastAPI
import json
from fastapi.responses import HTMLResponse  # html 형식으로 리턴해줌

def _get_auctions() -> list :
    with open('./auctions.json','r',encoding='utf-8') as f:
        return json.loads(f.read())

def _save_auctions(auctions: list):
    with open('./auctions.json','w',encoding='utf-8') as f:
       f.write(json.dumps(auctions,ensure_ascii=False))

app = FastAPI()

@app.get('/api/auctions')
def get_auctions():
    return _get_auctions()

@app.get('/auctions')
def get_auctions_html():
    with open('./auctions.html','r',encoding='utf-8') as f:
        return HTMLResponse(f.read())