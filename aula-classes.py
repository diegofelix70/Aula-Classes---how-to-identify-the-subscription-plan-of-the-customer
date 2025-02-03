class Cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.planos = ["basic", "premium"] # Aqui eu determino as opções de mensagens que pode ser usado na hora de estipular a msg
        if plano in self.planos:
            self.plano = plano
        else:
            print('Plano inválido')

    def mudar_plano(self, novo_plano):
        if novo_plano in self.planos:
            self.plano = novo_plano # Quando a função plano receber a novo_plano, ela vai continuar sendo plano
        else:
            print('Plano inválido')

    def ver_filme(self, filme, plano_filme): # Aqui ele vai puxar da váreavel plano_filme a lógica de dentro do programa
        if self.plano == plano_filme: # Aqui ele está chamando o plano filme para validar
            print(f"Ver filme {filme}")
        elif self.plano == "premium":
            print(f'Ver filme {filme}')
        elif self.plano == "basic" and plano_filme == "premium":
            print('Faça upgrade para premium para ver esse filme')
        else:
            print("Plano Inválido")


cliente = Cliente("Diego", "diego@email.com", "basic")
print(cliente.plano)
cliente.ver_filme("Harry Potter", "premium") # Com esse premium eu estipulo qual p parametro de corte

cliente.mudar_plano("premium") # Não chamei o cliente porque a vareavel já estava estabelecida, aqui eu somente alterei um parametro que já estava estipulado.
print(cliente.plano)
cliente.ver_filme("Harry Potter", "premium")
