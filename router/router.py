from fastapi import APIRouter, Response
from starlette.status import HTTP_201_CREATED
from starlette.status import HTTP_200_OK
from starlette.status import HTTP_206_PARTIAL_CONTENT
from schema.account_schema import AccountSchema
from config.db import engine
from model.account import modelAccount
from typing import List

account = APIRouter()


@account.get('/')
def root():
    return {"message": "router Client"}


""" FUNCION QUE RETORNA TODAS LAS CUENTAS """


@account.get('/api/account', response_model=List[AccountSchema])
def getAccounts():
    with engine.connect() as conn:
        result = conn.execute(modelAccount.select()).fetchall()
        return result


""" FUNCION QUE RETORNA UNA CUENTA BUSCADA """


@account.get('/api/account/{numberid}', response_model=AccountSchema)
def getAccount(numberid: int):
    with engine.connect() as conn:
        result = conn.execute(modelAccount.select().where(
            modelAccount.c.numberid == numberid)).first()
        return result


""" FUNCION PARA CREAR UNA NUEVA CUENTA """
@account.post('/api/account', status_code=HTTP_201_CREATED)
def createAccount(data_account: AccountSchema):
    account = getAccount(data_account.numberid)
    if not account:
        with engine.connect() as conn:
            new_account = data_account.dict()
            conn.execute(modelAccount.insert().values(new_account))
            return Response(status_code=HTTP_201_CREATED)
    else:
        return Response(status_code=HTTP_206_PARTIAL_CONTENT)


""" FUNCION PARA ACTUALIZAR EL VALOR """
@account.put('/api/account/{numberid}', response_model=AccountSchema, status_code=HTTP_200_OK)
def updateAccount(data_account: AccountSchema, numberid: int):
    with engine.connect() as conn:
        conn.execute(modelAccount.update().values(current =data_account.current).where(modelAccount.c.numberid == numberid))
        result = getAccount(numberid)

        return result
