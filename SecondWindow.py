from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QCheckBox


class Comp490DataDemoWindow(QWidget):

    def __init__(self, data_to_show: dict):
        super().__init__()
        self.data = data_to_show
        self.checkbox = QCheckBox(self)
        self.setup_window()

    def setup_window(self):
        self.setWindowTitle("Detail about selected list")
        self.setGeometry(900, 300, 300, 500)  # put the new window next to the original one wider than it is tall
        v_layout = QVBoxLayout(self)
        label = QLabel(self)

        # for i in range(2, 13):
        #     option = self.data[f'Field{i}']
        #     if option != '':
        #         label.setText(option)

        # Prefix
        label.setText("Prefix:")
        display = QLineEdit(self.data['Field2'], self)
        display.setReadOnly(True)  # create QLineEdit uneditable
        v_layout.addWidget(label)
        v_layout.addWidget(display)

        # First Name
        label = QLabel("First Name:", self)
        display = QLineEdit(self.data['Field4'], self)
        display.setReadOnly(True)
        v_layout.addWidget(label)
        v_layout.addWidget(display)

        # Last Name
        label = QLabel("Last Name:", self)
        display = QLineEdit(self.data['Field5'], self)
        display.setReadOnly(True)
        v_layout.addWidget(label)
        v_layout.addWidget(display)

        # Title
        label = QLabel("Title:", self)
        display = QLineEdit(self.data['Field6'], self)
        display.setReadOnly(True)
        v_layout.addWidget(label)
        v_layout.addWidget(display)

        # Organization Name
        label = QLabel("Organization:", self)
        display = QLineEdit(self.data['Field7'], self)
        display.setReadOnly(True)
        v_layout.addWidget(label)
        v_layout.addWidget(display)

        # Email
        label = QLabel("Email:", self)
        display = QLineEdit(self.data['Field12'], self)
        display.setReadOnly(True)
        v_layout.addWidget(label)
        v_layout.addWidget(display)

        # Website
        label = QLabel("Website:", self)
        display = QLineEdit(self.data['Field9'], self)
        display.setReadOnly(True)
        v_layout.addWidget(label)
        v_layout.addWidget(display)

        # Phone Number
        label = QLabel("Phone#:", self)
        display = QLineEdit(self.data['Field10'], self)
        display.setReadOnly(True)
        v_layout.addWidget(label)
        v_layout.addWidget(display)

        # Intresting 1 - 7
        option_list = ['Course Project', 'Guest Speaker', 'Site Visit', 'Job Shadow', 'Internship', 'Career Panel', 'Networking Event']
        for i in range(14, 21):
            option = self.data[f'Field{i}']
            if option != '':
                self.checkbox = QCheckBox(f"{option_list[14-i]}", self)
                self.checkbox.setChecked(True)
                self.checkbox.toggled.connect(self.prevent_toggle)
            else:
                self.checkbox = QCheckBox(f"{option_list[14-i]}", self)
                self.checkbox.toggled.connect(self.prevent_toggle)

            v_layout.addWidget(self.checkbox)

        # Collaboration time period
        label = QLabel("Proposed collaboration time period")
        v_layout.addWidget(label)
        for i in range(114, 119):
            line = self.data[f'Field{i}']
            if line != '':
                display = QLineEdit(line, self)
                display.setReadOnly(True)
                v_layout.addWidget(display)

        # Description
        label = QLabel("CUBES Project Description")
        v_layout.addWidget(label)
        display = QLineEdit(self.data['Field214'], self)
        display.setReadOnly(True)
        v_layout.addWidget(display)

    def prevent_toggle(self):
        self.checkbox.setChecked(Qt.Checked)
