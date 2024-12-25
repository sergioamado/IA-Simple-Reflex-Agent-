import random

from Environment0 import Environment

# As duas localizações para o mundo do aspirador de pó
loc_A, loc_B = (0, 0), (1, 0)

class TrivialVacuumEnvironment(Environment):
    """Este ambiente tem duas localizações, A e B. Cada uma pode estar Suja ou Limpa.
    O agente percebe sua localização e o estado dessa localização.
    Este é um exemplo de como implementar um Ambiente simples."""

    def __init__(self):
        # Inicializa o ambiente com estados aleatórios para as duas localizações.
        super().__init__()
        self.status = {loc_A: random.choice(['Clean', 'Dirty']),
                       loc_B: random.choice(['Clean', 'Dirty'])}

    def thing_classes(self):
        # Retorna uma lista das classes de objetos que podem estar presentes no ambiente.
        # Estas classes devem ser implementadas separadamente.
        return [Wall, Dirt, ReflexVacuumAgent, RandomVacuumAgent, TableDrivenVacuumAgent, ModelBasedVacuumAgent]

    def percept(self, agent):
        """Retorna a localização do agente e o estado da localização (Sujo/Limpo)."""
        print(f"    Localização do agente: {agent.location}")
        return agent.location, self.status[agent.location]

    def execute_action(self, agent, action):
        """Altera a localização do agente e/ou o estado da localização; rastreia o desempenho.
        Pontuações: +10 para cada sujeira limpa; -1 para cada movimento realizado."""
        print(f"    Ação a ser realizada: {action}")
        if action == 'Right':  # Move o agente para a direita
            agent.location = loc_B
            agent.performance -= 1
        elif action == 'Left':  # Move o agente para a esquerda
            agent.location = loc_A
            agent.performance -= 1
        elif action == 'Suck':  # Limpa a sujeira na localização atual
            if self.status[agent.location] == 'Dirty':
                agent.performance += 10
            self.status[agent.location] = 'Clean'
