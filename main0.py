import random  # Importa o módulo random para gerar escolhas aleatórias

from Agent0 import Agent  # Importa a classe Agent do módulo Agent0
from Environment0 import (
    Environment,
)  # Importa a classe Environment do módulo Environment0
from TrivialVacuumEnvironment0 import (
    TrivialVacuumEnvironment,
)  # Importa a classe TrivialVacuumEnvironment do módulo correspondente


# Função para testar funcionalidades básicas da classe Environment
def test_environment():
    v = Environment()  # Cria uma instância da classe Environment
    v.is_done()  # Verifica se o ambiente está finalizado
    v.step()  # Realiza uma etapa no ambiente
    v.run()  # Executa o ambiente por um número padrão de etapas


# Função para testar funcionalidades básicas da classe Agent
def test_agent():
    # Define um programa de agente constante que retorna exatamente o percept recebido
    def constant_prog(percept):
        return percept

    agent = Agent(constant_prog)  # Cria um agente com o programa definido
    result = agent.program(
        5
    )  # Aplica o programa do agente a um percept (neste caso, 5)
    assert (
        result == 5
    )  # Verifica se o resultado do programa é igual ao percept fornecido


test_environment()  # Executa o teste da classe Environment
test_agent()  # Executa o teste da classe Agent


# Função para testar a adição de agentes ao ambiente
def test_inseriragentenoambiente():
    v = Environment()  # Cria uma instância do ambiente
    agent = Agent()  # Cria um agente
    agent2 = Agent()  # Cria um segundo agente

    o = v.is_done()  # Verifica se o ambiente está finalizado
    print("    Sem agente is_done={}".format(o))  # Imprime o estado inicial do ambiente

    v.add_thing(
        agent, "area1"
    )  # Adiciona o primeiro agente ao ambiente em uma localização específica
    v.add_thing(agent2, "area1")  # Adiciona o segundo agente à mesma localização

    o = v.is_done()  # Verifica novamente se o ambiente está finalizado
    print(
        "    Com agente inserido is_done={}".format(o)
    )  # Imprime o novo estado do ambiente

    # Teste comentado porque depende de implementar o método percept()
    # v.step()
    # v.run()

    # Lista todas as coisas presentes na localização "area1"
    allthings = v.list_things_at("area1")
    print(
        f"Lista de coisas dentro do ambiente:{allthings}"
    )  # Exibe a lista de coisas no ambiente


test_inseriragentenoambiente()  # Executa o teste de inserção de agentes


# Define um programa de agente que escolhe uma ação aleatória da lista fornecida
def RandomAgentProgram(actions):
    return lambda percept: random.choice(
        actions
    )  # Retorna uma função que escolhe aleatoriamente uma ação


# Função para testar o TrivialVacuumEnvironment
def test_trivialvacuumenvironment():
    v = TrivialVacuumEnvironment()  # Cria uma instância do TrivialVacuumEnvironment

    list = ["Right", "Left", "Suck", "NoOp"]  # Define as ações possíveis para o agente
    program = RandomAgentProgram(list)  # Cria um programa de agente com essas ações

    agent = Agent(program)  # Cria um agente usando o programa definido

    v.add_thing(
        agent, location=(0, 0)
    )  # Adiciona o agente ao ambiente na posição inicial (0,0)

    # Imprime o desempenho inicial e o estado inicial do ambiente
    print("\n")
    print("Desempenho: {}".format(agent.performance))
    print(f"    status mundo:  {v.status}")

    # Executa várias etapas e exibe o desempenho do agente e o estado do ambiente
    v.step()
    print("Desempenho: {}".format(agent.performance))
    print(f"    status mundo:  {v.status}")

    v.step()
    print("Desempenho: {}".format(agent.performance))
    print(f"    status mundo:  {v.status}")

    v.step()
    print("Desempenho: {}".format(agent.performance))
    print(f"    status mundo:  {v.status}")

    v.step()
    print("Desempenho: {}".format(agent.performance))
    print(f"    status mundo:  {v.status}")

    # Teste de execução contínua comentado
    # v.run(10)


test_trivialvacuumenvironment()  # Executa o teste do TrivialVacuumEnvironment
