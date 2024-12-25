import numbers  # Importa o módulo numbers, usado para verificar se um valor é numérico.

from Thing0 import Thing  # Importa a classe base Thing do módulo Thing0, representando objetos no ambiente.
from Agent0 import Agent  # Importa a classe Agent do módulo Agent0, que herda de Thing.

class Environment:
    """Classe abstrata que representa um Ambiente. Classes reais de ambiente
    devem herdar desta classe. Um ambiente precisa implementar:
        percept:           Define o percepto que um agente observa.
        execute_action:    Define os efeitos de executar uma ação.
                           Também atualiza o atributo agent.performance.
    O ambiente mantém uma lista de .things (objetos) e .agents (um subconjunto
    de .things). Cada agente tem um atributo .performance inicializado como 0.
    Cada objeto tem um atributo .location, embora nem todos os ambientes
    possam precisar disso."""

    def __init__(self):  # Inicializa o ambiente.
        self.things = []  # Lista de todos os objetos no ambiente.
        self.agents = []  # Lista de agentes no ambiente.

    def thing_classes(self):  # Método para listar as classes de objetos permitidas no ambiente.
        return []  # Retorna uma lista vazia por padrão.

    def percept(self, agent):  # Define o percepto que o agente percebe no momento.
        """Retorna o percepto que o agente observa. (Deve ser implementado.)"""
        raise NotImplementedError  # Levanta um erro para ser implementado em subclasses.

    def execute_action(self, agent, action):  # Define os efeitos de uma ação no ambiente.
        """Altera o estado do mundo para refletir essa ação. (Deve ser implementado.)"""
        raise NotImplementedError  # Levanta um erro para ser implementado em subclasses.

    def default_location(self, thing):  # Define a localização padrão de um objeto.
        """Localização padrão para um novo objeto sem localização especificada."""
        return None  # Por padrão, retorna None.

    def exogenous_change(self):  # Representa mudanças espontâneas no ambiente.
        """Se houver mudanças espontâneas no mundo, este método deve ser sobrescrito."""
        pass  # Não faz nada por padrão.

    def is_done(self):  # Determina se o ambiente deve parar de funcionar.
        """Por padrão, o ambiente para quando não há mais agentes vivos."""
        return not any(agent.is_alive() for agent in self.agents)  # Verifica se algum agente está vivo.

    def step(self):  # Executa o ambiente por um único passo de tempo.
        """Executa o ambiente por um passo de tempo. Se as ações e mudanças exógenas
        forem independentes, este método será suficiente. Caso contrário,
        precisa ser sobrescrito."""
        if not self.is_done():  # Verifica se o ambiente ainda está ativo.
            actions = []  # Lista de ações dos agentes.
            for agent in self.agents:  # Itera sobre os agentes no ambiente.
                if agent.alive:  # Se o agente estiver vivo...
                    actions.append(agent.program(self.percept(agent)))  # Obtém a ação do programa do agente.
                else:  # Caso contrário, adiciona uma ação vazia.
                    actions.append("")
            for (agent, action) in zip(self.agents, actions):  # Itera sobre agentes e ações.
                self.execute_action(agent, action)  # Executa cada ação no ambiente.
            self.exogenous_change()  # Aplica mudanças espontâneas no ambiente.

    def run(self, steps=1000):  # Executa o ambiente por um número especificado de passos.
        """Executa o ambiente por um número determinado de passos de tempo."""
        for step in range(steps):  # Itera pelos passos.
            if self.is_done():  # Para se o ambiente terminar.
                return
            self.step()  # Executa um único passo de tempo.

    def list_things_at(self, location, tclass=Thing):  # Lista objetos em uma localização específica.
        """Retorna todos os objetos em uma localização específica."""
        if isinstance(location, numbers.Number):  # Verifica se a localização é um número.
            return [thing for thing in self.things
                    if thing.location == location and isinstance(thing, tclass)]
        return [thing for thing in self.things
                if all(x == y for x, y in zip(thing.location, location)) and isinstance(thing, tclass)]

    def some_things_at(self, location, tclass=Thing):  # Verifica se há objetos de uma classe específica em uma localização.
        """Retorna True se pelo menos um objeto em uma localização
        for uma instância de tclass (ou de uma subclasse)."""
        return self.list_things_at(location, tclass) != []  # Retorna True se a lista não for vazia.

    def add_thing(self, thing, location=None):  # Adiciona um objeto ao ambiente.
        """Adiciona um objeto ao ambiente, configurando sua localização.
        Se o objeto for um programa de agente, cria um novo agente para ele."""
        if not isinstance(thing, Thing):  # Verifica se o objeto não é uma instância de Thing.
            thing = Agent(thing)  # Converte o objeto em um agente.
        if thing in self.things:  # Verifica se o objeto já está no ambiente.
            print("Não é possível adicionar o mesmo objeto duas vezes.")
        else:  # Caso contrário, adiciona o objeto.
            thing.location = location if location is not None else self.default_location(thing)  # Define a localização.
            self.things.append(thing)  # Adiciona à lista de objetos.
            if isinstance(thing, Agent):  # Se o objeto for um agente...
                thing.performance = 0  # Inicializa o desempenho.
                self.agents.append(thing)  # Adiciona à lista de agentes.

    def delete_thing(self, thing):  # Remove um objeto do ambiente.
        """Remove um objeto do ambiente."""
        try:
            self.things.remove(thing)  # Tenta remover o objeto da lista de objetos.
        except ValueError as e:  # Captura erro se o objeto não estiver na lista.
            print(e)  # Exibe o erro.
            print("  em delete_thing do Ambiente")  # Mensagem informativa.
            print("  Objeto a ser removido: {} em {}".format(thing, thing.location))  # Detalhes do objeto.
            print("  da lista: {}".format([(thing, thing.location) for thing in self.things]))  # Detalhes da lista.
        if thing in self.agents:  # Remove o objeto da lista de agentes, se necessário.
            self.agents.remove(thing)
