from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QDialogButtonBox,
    QLineEdit,
    QFormLayout,
    QMessageBox
)


class InputDialog(QDialog):
    def __init__(self, parent: None):
        super().__init__(parent=parent)
        self.setWindowTitle('Input Dialog')
        self.window_layout: QVBoxLayout = None
        self.buttonsBox: QDialogButtonBox = None
        self.claim_fn: QLineEdit = None
        self.claim_ln: QLineEdit = None
        self.claim_title: QLineEdit = None
        self.claim_email: QLineEdit = None
        self.claim_dept: QLineEdit = None
        self.data = None
        self.get_input()

    def get_input(self):
        self.window_layout = QVBoxLayout()

        self.claim_fn = QLineEdit()
        self.claim_fn.setObjectName("First Name")
        self.claim_ln = QLineEdit()
        self.claim_fn.setObjectName("Last Name")
        self.claim_title = QLineEdit()
        self.claim_fn.setObjectName("Title")
        self.claim_email = QLineEdit()
        self.claim_fn.setObjectName("BSU Email")
        self.claim_dept = QLineEdit()
        self.claim_fn.setObjectName("Department")

        form_layout = QFormLayout()
        form_layout.addRow("First Name", self.claim_fn)
        form_layout.addRow("Last Name", self.claim_ln)
        form_layout.addRow("Title", self.claim_title)
        form_layout.addRow("Email", self.claim_email)
        form_layout.addRow("Department", self.claim_dept)
        self.window_layout.addLayout(form_layout)

        self.buttonsBox = QDialogButtonBox()
        self.buttonsBox.setOrientation(Qt.Horizontal)
        self.buttonsBox.setStandardButtons(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        )
        self.buttonsBox.accepted.connect(self.accept)
        self.buttonsBox.rejected.connect(self.reject)
        self.window_layout.addWidget(self.buttonsBox)

        self.setLayout(self.window_layout)

    def accept(self):
        self.data = []
        for box in (self.claim_fn, self.claim_ln, self.claim_title, self.claim_email, self.claim_dept):
            # If given data is not valid
            if not box.text():
                QMessageBox.critical(
                    self,
                    "Error!",
                    f"You must provide a information for '{box.objectName()}'\nIf you are not sure what to enter, leave the field with 'N/A'",
                )
                # Reset .data
                self.data = None
                return

            self.data.append(box.text())

        if not self.data:
            return

        super().accept()

    def user_input(self):
        if self.exec_() == QDialog.Accepted:
            return self.data
        else:
            return None
