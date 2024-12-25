class Thing:
    """Esta classe representa qualquer objeto físico que pode aparecer em um Ambiente.
    Você pode criar subclasses de Thing para definir os objetos desejados. 
    Cada objeto pode ter um atributo .__name__ (usado apenas para fins de exibição)."""

    def __repr__(self):
        # Define como o objeto será exibido quando impresso.
        # Exibe o valor do atributo '__name__' se ele existir; caso contrário, exibe o nome da classe.
        return '<{}>'.format(getattr(self, '__name__', self.__class__.__name__))

    def is_alive(self):
        """Coisas que estão 'vivas' devem retornar True."""
        # Verifica se o objeto tem o atributo 'alive' e se seu valor é True.
        return hasattr(self, 'alive') and self.alive

    def show_state(self):
        """Exibe o estado interno do agente. Subclasses devem sobrescrever este método."""
        # Método padrão que imprime uma mensagem informando que não sabe como mostrar o estado.
        print("Não sei como mostrar o estado.")

    def display(self, canvas, x, y, width, height):
        """Exibe uma imagem deste objeto em um canvas."""
        # Este método pode ser sobrescrito em subclasses para exibir o objeto em um ambiente gráfico.
        # Atualmente, não faz nada.
        pass
