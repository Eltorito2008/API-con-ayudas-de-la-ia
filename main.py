from fastapi import FastAPI
from routers import clientes_router, productos_router, pedidos_router

app = FastAPI(title="Carrito de Compra API", version="1.0.0")

# Incluir routers
app.include_router(clientes_router.router)
app.include_router(productos_router.router)
app.include_router(pedidos_router.router)

@app.get("/")
def root():
    return {"message": "Bienvenido a la API del Carrito de Compra"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}