import sys

from PyQt6.QtWidgets import (
    QApplication,
    QDialog,
    QDialogButtonBox,
    QLineEdit,
    QLabel,
    QVBoxLayout,
)

class PopUp_Window(QDialog):
    def __init__(self, error_message):
        super().__init__()

        self.setWindowTitle("Error")


        self.buttons = QDialogButtonBox()
        self.buttons.setStandardButtons(
            QDialogButtonBox.StandardButton.Ok
        )

        self.buttons.accepted.connect(self.accept)

        layout = QVBoxLayout()
        ERROR_CONST = QLabel("Error")
        message = QLabel(error_message)
        layout.addWidget(ERROR_CONST)
        layout.addWidget(message)
        layout.addWidget(self.buttons)
        self.setLayout(layout)

def Activate_PopUp(message: str):
    window = PopUp_Window(message)
    window.exec()

