from pathlib import Path
CAMINHO_ARQUIVO = Path(__file__).parent / 'file.txt'
class Log:
    def _log(self, msg):
        raise NotImplementedError('implemente o método log')
    def log_error(self, msg):
        return self._log(f'error: {msg}')
    def log_success(self, msg):
        return self._log(f'susseco: {msg} ')
class LogFileMixin(Log):
    def _log(self, msg):
        msg_formatada = f'{msg} ({self.__class__.__name__})'
        with open(CAMINHO_ARQUIVO, 'a') as arquivo:
            arquivo.write(msg_formatada)
            arquivo.write('\n')
class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')
if __name__ == '__main__':
    lp = LogPrintMixin()
    lp.log_error('qualquer coisa')
    lp.log_success('Que legal')
    lf = LogFileMixin()
    lf.log_error('qualquer coisa')
    lf.log_success('Que legal')
    lf.log_error('vai se fuder')