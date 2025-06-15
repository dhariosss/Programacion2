usuarios = {
    "juan": "1234",
    "maria": "abcd"
}

def verificar_usuario(nombre, clave):
    return usuarios.get(nombre) == clave
