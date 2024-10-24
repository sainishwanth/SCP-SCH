import sys

from PyQt6.QtWidgets import (
    QApplication,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QLineEdit,
    QVBoxLayout,
)

from PopUp import Activate_PopUp

class client_Window_class(QDialog):
    def __init__(self):
        super().__init__(parent=None)
        self.setWindowTitle("Client Window")

        dialogLayout = QVBoxLayout()
        formLayout = QFormLayout()
        self.path_client = QLineEdit()
        formLayout.addWidget(self.path_client)
        
        dialogLayout.addLayout(formLayout)

        self.buttons = QDialogButtonBox()
        self.buttons.setStandardButtons(
            QDialogButtonBox.StandardButton.Cancel
            | QDialogButtonBox.StandardButton.Ok
        )

        self.buttons.accepted.connect(self.submit)
        self.buttons.rejected.connect(self.cancel)

        dialogLayout.addWidget(self.buttons)
        self.setLayout(dialogLayout)




    def submit(self):
        if self.path_client.text() == '':
            Activate_PopUp("No Path Provided")
        else:
            pass

    def cancel(self):
        self.reject()


