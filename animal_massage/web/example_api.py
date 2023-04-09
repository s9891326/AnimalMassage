from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, EmailStr

app = FastAPI()


# path variables
# https://fastapi.tiangolo.com/tutorial/path-params/
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


# query string
# https://fastapi.tiangolo.com/tutorial/query-params/#__tabbed_4_2
@app.get("/items_with_params/{item_id}")
async def read_user_item(
        item_id: str, needy: str, skip: int = 0, limit: int | None = None
):
    # Note: mixed path variables with query string
    #
    # path variables:
    # item_id is a path variable, others are query string which don't present on the URI
    #
    # query string:
    # * needy => required, because without a default value
    # * skip => optional by a default value, client could ignore it
    # * limit => optional for int or a default None value
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item


# Example for request body
# https://fastapi.tiangolo.com/tutorial/body/
#
# note: it could be mixed with either path variables or query string
# https://fastapi.tiangolo.com/tutorial/body-multiple-params/


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.post("/items/")
async def create_item(item: Item):
    return item


# Example for response model
# https://fastapi.tiangolo.com/tutorial/response-model/
class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str | None = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


@app.post("/user/", response_model=UserOut)
async def create_user(user: UserIn):
    # password will not go to the response
    return user


# https://fastapi.tiangolo.com/tutorial/body-updates/?h=patch#using-pydantics-update-parameter
class Item(BaseModel):
    name: str | None = None
    description: str | None = None
    price: float | None = None
    tax: float = 10.5
    tags: list[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


@app.get("/items2/{item_id}", response_model=Item)
async def read_item(item_id: str):
    return items[item_id]


@app.patch("/items2/{item_id}", response_model=Item)
async def update_item(item_id: str, item: Item):
    stored_item_data = items[item_id]
    stored_item_model = Item(**stored_item_data)
    update_data = item.dict(exclude_unset=True)
    updated_item = stored_item_model.copy(update=update_data)
    items[item_id] = jsonable_encoder(updated_item)
    return updated_item


@app.delete("/items2/{item_id}")
async def delete_item(item_id: str):
    delete_item_data = items.get(item_id)
    if not delete_item_data:
        return False

    items.pop(item_id)
    return True
