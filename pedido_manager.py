from pydantic import BaseModel
import psycopg

class Pedido(BaseModel):
    id_pedido: int
    id_producto: int
    id_cliente: int

class PedidoManager:
    def insertar_pedido(self, pedido: Pedido, cursor: psycopg.Cursor):
        cursor.execute(
            "INSERT INTO pedido (id_pedido, id_cliente, id_producto) VALUES (%s, %s, %s)",
            (pedido.id_pedido, pedido.id_cliente, pedido.id_producto)
        )
        return {"mensaje": "Pedido insertado"}

    def eliminar_pedido(self, id_pedido: int, cursor: psycopg.Cursor):
        cursor.execute("DELETE FROM pedido WHERE id_pedido = %s", (id_pedido,))
        return {"mensaje": f"Pedido {id_pedido} eliminado"}

    def mostrar_pedidos(self, cursor: psycopg.Cursor):
        cursor.execute("""
            SELECT p.id_pedido, c.nombre, c.apellido, pr.nombre, pr.precio 
            FROM pedido p 
            INNER JOIN cliente c ON p.id_cliente = c.id_cliente 
            INNER JOIN productos pr ON p.id_producto = pr.id_producto
        """)
        return [{
            "id_pedido": row[0],
            "cliente_nombre": row[1],
            "cliente_apellido": row[2],
            "producto_nombre": row[3],
            "producto_precio": row[4]
        } for row in cursor.fetchall()]