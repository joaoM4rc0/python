from abc import ABC, abstractmethod

class CalculoBase(ABC):
    def __init__(self):
        self._val = 4
    @property
    def val(self):
        return self._val
    @val.setter
    def val(self, x):
        self._val_setter(x)
    @abstractmethod
    def _val_setter(self, x):
        ...
class filhaBase(CalculoBase):
    def _val_setter(self, x):
        self._val = 4 * x
base = filhaBase()
base.val = 8
print(base.val)