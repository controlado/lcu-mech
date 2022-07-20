# `🦕` `LCU`

### About me:
- ![info](https://img.shields.io/static/v1?logo=discord&label=&message=Balaclava%231912&color=00d26a&logoColor=white&style=flat)
- ![languages](https://img.shields.io/static/v1?logo=Python&label=&message=Python%203.10.5&color=00d26a&logoColor=white&style=flat)
![languages3](https://img.shields.io/static/v1?label=&message=Requests&color=00d26a&logoColor=white&style=flat)
- ![ide](https://img.shields.io/static/v1?logo=Visual%20Studio%20Code&label=&message=Visual%20Studio%20Code&color=00d26a&logoColor=white&style=flat)
![ide1](https://img.shields.io/static/v1?logo=Github&label=&message=License%20Apache%202.0&color=00d26a&logoColor=white&style=flat)

#

### Built-in methods:

<details>
  <summary>✅ (unlock_champions) </summary>

  ```python
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
  ```

</details>

<details>
  <summary>✅ (unlock_champions_tag) </summary>

  ```python
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
  ```

</details>

<details>
  <summary>✅ (unlock_champions_names) </summary>

  ```python
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
  ```

</details>

<details>
  <summary>✅ (unlock_champions_ea) </summary>

  ```python
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
  ```

</details>

### Installation:
- Download the source and Python latest version
- Paste `pip install -r requirements.txt` in terminal
