from typing import Callable


class Item:
    def __init__(self, nome: str, valor: int):
        self.nome = nome
        self.valor = valor

    def __repr__(self):
        return f'Item({self.nome}, {self.valor})'

class Carrinho:
    def  __init__(self):
        self.itens = []

    def adicionar_item(self, item: Item):
        self.itens.append(item)

    @property
    def valor(self):
        return sum(map(lambda item: item.valor, self.itens))


def promocao_10(carrinho: Carrinho):
    if carrinho.valor > 1_000:
        return carrinho.valor - (carrinho.valor * 0.1)


def promocao_5(carrinho: Carrinho):
    if len(carrinho.itens) >= 5:
        return carrinho.valor - (carrinho.valor * 0.05)


class Promocoes:
    def __init__(self, *promos: Callable):
        self.promos = promos

    def __call__(self, carrinho: Carrinho):
        for promo in self.promos:
            if (resultado := promo(carrinho)):
                return resultado

        return self.fallback(carrinho)

    def fallback(self, carrinho: Carrinho):
        return carrinho.valor



c = Carrinho()

p = Promocoes(promocao_10, promocao_5)

c.adicionar_item(Item('fritas', 100))
c.adicionar_item(Item('fritas', 100))
c.adicionar_item(Item('fritas', 100))
c.adicionar_item(Item('fritas', 100))
c.adicionar_item(Item('fritas', 100))
c.adicionar_item(Item('fritas', 1000))

print(c.valor)
print(p(c))
