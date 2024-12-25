import collections  # Importa o módulo collections para verificar se um programa é chamável (Callable).

from Thing0 import (
    Thing,
)  # Importa a classe base Thing do módulo Thing0, usada para representar objetos no ambiente.


class Agent(Thing):
    """Um Agente é uma subclasse de Thing com um slot obrigatório, .program,
    que deve conter uma função que recebe um argumento (o percepto) e retorna uma ação.
    (O que é considerado um percepto ou uma ação depende do ambiente em que o agente existe.)
    'program' é um slot, não um método. Isso significa que o programa não pode acessar
    informações internas do agente; ele só pode usar os perceptos fornecidos.
    Um programa de agente que precisa de um modelo do mundo ou do próprio agente
    deve construir e manter esse modelo separadamente.
    O agente também pode ter um slot opcional, .performance, que mede seu desempenho no ambiente.
    """

    def __init__(self, program=None):  # Método inicializador para criar um agente.
        self.alive = True  # Atributo que indica se o agente está vivo.
        self.bump = False  # Atributo que indica se o agente colidiu com algo.
        self.holding = []  # Lista de itens que o agente está segurando.
        self.performance = 0  # Medida do desempenho do agente no ambiente.

        # Verifica se o programa é válido; caso contrário, define um programa padrão.
        if program is None or not isinstance(program, collections.abc.Callable):
            # Exibe uma mensagem informando que um programa válido não foi encontrado.
            print(
                "\n    Não foi possível encontrar um programa válido para {}, usando o padrão.".format(
                    self.__class__.__name__
                )
            )

            # Define um programa padrão que solicita ao usuário uma ação com base no percepto.
            def program(percept):
                return eval(input("Percept={}; ação? ".format(percept)))

        self.program = program  # Define o programa do agente.

    def can_grab(
        self, thing
    ):  # Método para verificar se o agente pode pegar um objeto.
        """Retorna True se este agente puder pegar este objeto.
        Este método pode ser sobrescrito em subclasses específicas de Agent e Thing."""
        return False  # Por padrão, o agente não pode pegar objetos.
