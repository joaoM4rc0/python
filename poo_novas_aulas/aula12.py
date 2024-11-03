class Upper_str(str):
    def upper(self):
        print('voce chamou a função upper')
        return super().upper()
pessoa = Upper_str('joao')
print(pessoa.upper())