'''
O Molde do Herói (Classes e Orientação a Objetos)

No desenvolvimento back-end e em jogos, 
usamos Classes como se fossem moldes de fábrica para criar vários objetos parecidos. 
Crie uma classe chamada Heroi que tenha um construtor (__init__) para receber o nome e 
a classe_jogo (por exemplo: "Mago" ou "Guerreiro"). 
Depois, crie um método chamado atacar dentro dessa classe que retorne a frase exata: 
"[Nome] usou ataque especial de [Classe]!".

'''

class Heroi:
    def __init__(self, nome: str, classe_jogo:str):
        self.nome: nome
        self.classe__jogo:  classe_jogo

    def atacar(self):
        return f"{self.nome} usou ataque especial de {self.classe__jogo} !"
        