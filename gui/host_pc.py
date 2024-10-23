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
        formLayout = QFormLayout()
        formLayout.addRow("hostname", QLineEdit())
        formLayout.addRow("address", QLineEdit())
        formLayout.addRow("Path", QLineEdit())
        formLayout.addRow("password", QLineEdit())

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

    def submit(self):
        print("Submit Clicked")
        self.accept()  # Close the dialog

    def cancel(self):
        self.reject()  # Close the dialog
