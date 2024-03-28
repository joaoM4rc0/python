from abc import ABC, abstractmethod
class Notificacao(ABC):
    def __init__(self, mensagem) -> None:
        self.mensagem = mensagem
    @abstractmethod
    def enviar(self) -> bool:...
class notificacaoEmail(Notificacao):
    def enviar(self) -> bool:
        print('E-mail: enviado -', self.mensagem)
        return True
class notificacaoSms(Notificacao):
    def enviar(self) -> bool:
        print('Sms: enviado -', self.mensagem)
        return False
def notificar(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar()
    if notificacao_enviada:
        print('Notificação enviada')
    else:
        print('Notificação NÃO enviada')
notificar(notificacaoEmail('teatando e-mail'))