from fastapi import APIRouter, Depends
import psycopg
from database.db_manager import get_db_cursor
from managers.cliente_manager import ClienteManager, Cliente

router = APIRouter(prefix="/clientes", tags=["Clientes"])
cliente_manager = ClienteManager()

@router.get("/")
def obtener_clientes(cursor: psycopg.Cursor = Depends(get_db_cursor)):
    return cliente_manager.mostrar_clientes(cursor)

@router.post("/")
def agregar_cliente(cliente: Cliente, cursor: psycopg.Cursor = Depends(get_db_cursor)):
    return cliente_manager.agregar_cliente(cliente, cursor)

@router.put("/{id_cliente}")
def modificar_cliente(id_cliente: int, cliente: Cliente, cursor: psycopg.Cursor = Depends(get_db_cursor)):
    return cliente_manager.modificar_cliente(id_cliente, cliente, cursor)

@router.delete("/{id_cliente}")
def eliminar_cliente(id_cliente: int, cursor: psycopg.Cursor = Depends(get_db_cursor)):
    return cliente_manager.eliminar_cliente(id_cliente, cursor)