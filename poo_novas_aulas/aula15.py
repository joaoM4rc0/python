from abc import ABC, abstractmethod

class Log(ABC):
    @abstractmethod
    def _log(self, msg):...
    def log_error(self, msg):
        return self._log(f'error: {msg}')
    def log_success(self, msg):
        return self._log(f'susseco: {msg} ')
class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')
l = LogPrintMixin()
l.log_error('olá')