from fastapi import FastAPI
import fastapi

app=FastAPI()

@app.get('/')
def index():
    return {'data': {'name':'Harish'}}


@app.get('/about')
def about():
    return {'date': 'Bhanu'}