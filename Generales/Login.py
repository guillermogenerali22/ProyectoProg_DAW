from Recursos.Configuracion import USUARIO, CONTRASEÑA

#Validando inicio de sesion
class Login:
    def __init__(self, usuario, contraseña):
        self._usuario = usuario
        self._contraseña = contraseña

    def validate(self):
        return self._usuario == USUARIO and self._contraseña == CONTRASEÑA

