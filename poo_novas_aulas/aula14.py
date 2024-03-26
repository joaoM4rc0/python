class A:
    def quem_sou(self):
        print('A')
class B:
    def quem_sou(self):
        print('B')
class C(A):
    def quem_sou(self):
        print('C')
class D(C, B):
    ...
    #herança multipla
    # def quem_sou(self):
    #     print('D')
d = D()
d.quem_sou()