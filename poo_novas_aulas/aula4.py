class Camera:
    def __init__(self, nome, filmando =False):
        self.nome = nome
        self.filmando = filmando
    def filmar(self) :
        if self.filmando:
            print('a camera está filmando')
            return
        self.filmando = True
    def parar_de_filmar(self):
        if not self.filmando:
            print('parando de filmar')
            return
        self.filmando = False
    def fotografia(self):
        if self.filmando:
            print('não pode fotografar gravando video')
            return
        print('está fotografando')
c1 = Camera('canon')
c1.filmar()
c1.filmar()
c1.fotografia()
c1.parar_de_filmar()
c1.fotografia()