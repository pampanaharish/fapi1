from fastapi import FastAPI
import fastapi

app=FastAPI()

@app.get('/')
def index():
    return {'data': {'name':'Harish'}}


@app.get('/about')
def about():
    return {'date': 'Bhanu'}

@app.get('/service')
def about():
    return {'date': 'Software development'}


@app.get('/blog/unpublished')    
def unpublished():
    return {'data':'All unpublished blogs'}


@app.get('/blog/{id}')
def show(id: int):
    return {'data': id}


@app.get('/blog/{id}/comments')
def comments(id):
    return {'data': {'1','2'}}    