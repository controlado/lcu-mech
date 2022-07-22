from PyQt5.QtWidgets import QLabel, QWidget, QPushButton, QGridLayout
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt
from tasks import Tasks

import sys


class Window(Tasks, QMainWindow):

    purchases = 0
    message = "Compras feitas:"

    def __init__(self):
        super().__init__()

        self.setFixedSize(300, 150)
        self.refresh_ui()

    def get_layout(self) -> QGridLayout:
        layout = QGridLayout()
        self.add_labels(layout)
        self.add_buttons(layout)
        return layout

    def get_refresh_button(self) -> QPushButton:
        button = QPushButton("Atualizar")
        button.clicked.connect(self.refresh_ui)
        button.setToolTip("Atualize a sua quantia de essência azul.")
        return button

    def get_champion_button(self, ea_cost: int) -> QPushButton:
        button = QPushButton(str(ea_cost))
        button.setToolTip(f"Comprar campeões com {ea_cost} de essência azul.")
        button.clicked.connect(lambda: self.on_click(ea_cost))
        button.setDisabled(not self.is_buyable(ea_cost))
        return button

    def add_labels(self, layout: QGridLayout) -> QGridLayout:
        label_1 = QLabel("Boas vindas ao Mech (desbloquear campeões)")
        label_2 = QLabel("Comprar campeões com quantas essências?")
        label_3 = QLabel("GitHub: Balasclava")
        label_4 = QLabel("Discord: Balaclava#1912")

        layout.addWidget(label_1, 0, 1, 1, 3, alignment=Qt.AlignCenter)
        layout.addWidget(label_2, 1, 1, 1, 3, alignment=Qt.AlignCenter)
        layout.addWidget(label_3, 4, 1, 1, 2, alignment=Qt.AlignLeft)
        layout.addWidget(label_4, 5, 1, 1, 2, alignment=Qt.AlignLeft)
        return layout

    def add_buttons(self, layout: QGridLayout) -> QGridLayout:
        layout.addWidget(self.get_champion_button(450), 2, 1, 1, 1)
        layout.addWidget(self.get_champion_button(1350), 2, 2, 1, 1)
        layout.addWidget(self.get_champion_button(3150), 2, 3, 1, 1)
        layout.addWidget(self.get_champion_button(4800), 3, 1, 1, 1)
        layout.addWidget(self.get_champion_button(6300), 3, 2, 1, 1)
        layout.addWidget(self.get_champion_button(7800), 3, 3, 1, 1)
        layout.addWidget(self.get_refresh_button(), 5, 3, 1, 1)
        return layout

    def is_buyable(self, ea_cost: int) -> bool:
        return self.get_wallet()["ip"] >= ea_cost

    def on_click(self, ea_cost: int):
        response = self.unlock_champions_ea(ea_cost)
        self.purchases += len(response)
        self.refresh_ui()

    def refresh_ui(self):
        self.setWindowTitle(f"{self.message} {self.purchases}")
        self.setup_window()

    def setup_window(self):
        widget = QWidget(self)
        widget.setLayout(self.get_layout())
        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    win = Window()
    win.show()

    sys.exit(app.exec_())
