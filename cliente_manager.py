from pydantic import BaseModel
import psycopg

class Cliente(BaseModel):
    nombre: str
    apellido: str

class ClienteManager:
    def agregar_cliente(self, cliente: Cliente, cursor: psycopg.Cursor):
        cursor.execute(
            "INSERT INTO cliente (nombre, apellido) VALUES (%s, %s)",
            (cliente.nombre, cliente.apellido)
        )
        return {"mensaje": f"Cliente '{cliente.nombre}' agregado"}

    def eliminar_cliente(self, id_cliente: int, cursor: psycopg.Cursor):
        cursor.execute("DELETE FROM cliente WHERE id_cliente = %s", (id_cliente,))
        return {"mensaje": f"Cliente {id_cliente} eliminado"}

    def modificar_cliente(self, id_cliente: int, cliente: Cliente, cursor: psycopg.Cursor):
        cursor.execute(
            "UPDATE cliente SET nombre = %s, apellido = %s WHERE id_cliente = %s",
            (cliente.nombre, cliente.apellido, id_cliente)
        )
        return {"mensaje": f"Cliente {id_cliente} actualizado"}

    def mostrar_clientes(self, cursor: psycopg.Cursor):
        cursor.execute("SELECT * FROM cliente")
        return [{"id_cliente": row[0], "nombre": row[1], "apellido": row[2]} for row in cursor.fetchall()]