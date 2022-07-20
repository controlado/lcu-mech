from lcu import LCU


class Tasks(LCU):

    def __init__(self):
        super().__init__()

    def unlock_champions(self, champions: list) -> list:
        """Compra uma lista de campeões.

        Utiliza as requisições necessárias pra comprar
        algum campeão e executa essa tarefa pra todos
        os campeões da lista.

        Também é feita uma verificação de essência azul,
        evitando assim, que o código tente comprar um
        campeão sem a quantidade de essência necessária.

        Parâmetros:
            champions: lista com os campeões: get_champions()

        Retorna:
            list: campeões que foram comprados.
        """
        return [self.unlock_champion(champion) for champion in champions if self.get_wallet()["ip"] >= champion["ipCost"]]

    def unlock_champions_tag(self, tag: str) -> list:
        """Compra os campeões que contém x tag.

        Para mais informações, consulte a documentação
        do método unlock_champions() da classe.

        Todas as tags possíveis no momento: [
            'ranged',
            '<<tag>>',
            'marksmen',
            'melee',
            'pusher',
            'requirement_owned',
            'void',
            'marksman',
            'support',
            'Zaun',
            'mage',
            'recommended',
            'carry',
            'fighter',
            'jungler',
            'stealth',
            'assassin',
            'tank'
        ]

        Parâmetros:
            tag: tag que deseja buscar os campeões.

        Retorna:
            list: campeões que foram comprados.
        """
        return self.unlock_champions([champion for champion in self.get_champions() if tag in champion["tags"]])

    def unlock_champions_names(self, names: list) -> list:
        """Compra os campeões que correspondem à lista de nomes.

        Para mais informações, consulte a documentação
        do método unlock_champions() da classe.

        Parâmetros:
            names: lista com os nomes dos campeões.

        Retorna:
            list: campeões que foram comprados.
        """
        return self.unlock_champions([champion for name in names for champion in self.get_champions() if champion["name"] == name])

    def unlock_champions_ea(self, ea_cost: int) -> list:
        """Compra os campeões que custam x essência azul.

        Para mais informações, consulte a documentação
        do método unlock_champions() da classe.

        Parâmetros:
            ea_cost: quantidade de essência azul.

        Retorna:
            list: campeões que foram comprados.
        """
        return self.unlock_champions([champion for champion in self.get_champions() if champion["ipCost"] == ea_cost])


if __name__ == "__main__":
    ea_cost = input("Digite um valor inteiro da quantia de essências. ")

    tasks = Tasks()
    r = tasks.unlock_champions_ea(ea_cost=ea_cost)

    input(f"{len(r)} campeões foram comprados.")
