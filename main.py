from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    item_id: int
    q: Union[str, None] = None


app = FastAPI()


@app.get('/items/{item_id}')
def read_item(item_id: int, q: Union[str, None] = None, response_model=Item):
    return {'item_id': item_id, 'q': q}
