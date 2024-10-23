import sys
from PyQt6.QtWidgets import (
    QApplication,
    QDialog,
    QGridLayout,
    QPushButton,
    QDialogButtonBox,
)
from client_pc import client_Window_class
from host_pc import host_Window_class

class Window(QDialog):
    def __init__(self):
        super().__init__(parent=None)
        self.setWindowTitle("Main Window")
        self.init_ui()
        self.create_layout()
        self.connect_signals()

    def init_ui(self):
        self.client_button = QPushButton("Client")
        self.host_button = QPushButton("Host")
        self.readme_button = QPushButton("Readme")
        self.dialog_buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)

    def create_layout(self):
        layout = QGridLayout()
        layout.addWidget(self.host_button, 0, 0)
        layout.addWidget(self.client_button, 0, 1)
        layout.addWidget(self.dialog_buttons, 1, 0)
        layout.addWidget(self.readme_button, 1, 1)
        self.setLayout(layout)

    def connect_signals(self):
        self.client_button.clicked.connect(self.open_client_window)
        self.host_button.clicked.connect(self.open_host_window)
        self.dialog_buttons.accepted.connect(self.accept)
        self.dialog_buttons.rejected.connect(self.reject)

    def open_host_window(self):
        host_window = host_Window_class()
        host_window.exec()

    def open_client_window(self):
        client_window = client_Window_class()
        client_window.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
