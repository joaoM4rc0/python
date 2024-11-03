class connection:
    def __init__(self, host='localhost'):
        self.host = host 
        self.user = None
        self.password = None

    def usuario(self, user):
        self.user = user
    def senha(self, password):
            self.password = password
    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection
# usuario = connection()
# usuario.usuario('joao')
# usuario.senha('1856JM')
usuario = connection.create_with_auth('joao', '1234')
print(usuario.host, usuario.user, usuario.password, sep='\n')