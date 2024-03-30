class Myopen:
    def __init__(self, caminho_arquivo, modo):
        self.caminho_arguivo = caminho_arquivo
        self.modo = modo
        self._arquivo = None
    def __enter__(self):
        print('ABRINDO ARQUIVO')
        self._arquivo = open(self.caminho_arguivo, self.modo, encoding='utf8')
        return self._arquivo
    def __exit__(self, class_exception, exception_, traceback_):
        print('FECHANDO ARQUIVO')
        self._arquivo.close() 
with Myopen('aula22.txt', 'w') as arquivo:
    print('WITH', arquivo)