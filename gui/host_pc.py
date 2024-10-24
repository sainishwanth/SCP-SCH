import sys
from PyQt6.QtWidgets import (
    QApplication,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QLineEdit,
    QVBoxLayout,
)

class host_Window_class(QDialog):
    def __init__(self):
        super().__init__(parent=None)
        self.setWindowTitle("Host Window")

        dialogLayout = QVBoxLayout()
        elements = self.init_elements()
        formLayout = self.add_elements_layout(elements)

        dialogLayout.addLayout(formLayout)

        buttons = QDialogButtonBox()
        buttons.setStandardButtons(
            QDialogButtonBox.StandardButton.Cancel
            | QDialogButtonBox.StandardButton.Ok
        )

        buttons.accepted.connect(self.submit)
        buttons.rejected.connect(self.cancel)

        dialogLayout.addWidget(buttons)
        self.setLayout(dialogLayout)


    def init_elements(self):
        self.hostname = QLineEdit()
        self.address = QLineEdit()
        self.path = QLineEdit()
        self.password = QLineEdit()

        return {self.hostname: "hostname",
                self.address: "address",
                self.path: "path",
                self.password: "password"}

    def add_elements_layout(self, elements: dict):
        formLayout = QFormLayout()
        for attribute, name in elements.items():
            formLayout.addRow(name, attribute)
        return formLayout


    def submit(self):
        print("Submit Clicked")
        self.accept()  # Close the dialog

    def cancel(self):
        self.reject()  # Close the dialog
