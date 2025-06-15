from fastapi import FastAPI, HTTPException, Depends, Header
from auth import crear_token, verificar_token
from users import verificar_usuario

app = FastAPI()

@app.post("/login")
def login(username: str, password: str):
    if verificar_usuario(username, password):
        token = crear_token({"sub": username})
        return {"access_token": token}
    raise HTTPException(status_code=401, detail="Credenciales inválidas")

@app.get("/protegido")
def recurso_protegido(Authorization: str = Header(...)):
    if not Authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Cabecera inválida")

    token = Authorization.split(" ")[1]
    resultado = verificar_token(token)
    if "error" in resultado:
        raise HTTPException(status_code=401, detail=resultado["error"])

    return {"mensaje": f"Acceso concedido a {resultado['sub']}"}
