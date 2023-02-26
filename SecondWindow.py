from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QVBoxLayout, QCheckBox


class SecondWindow(QWidget):

    def __init__(self, data_to_show: dict):
        super().__init__()
        self.data = data_to_show
        self.setup_window()

    def setup_window(self):
        self.setWindowTitle("Detail about selected list")
        self.setGeometry(600, 300, 300, 500)
        v_layout = QVBoxLayout(self)
        label = QLabel(self)

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
        option_list = ['Course Project', 'Guest Speaker', 'Site Visit', 'Job Shadow',
                         'Internship', 'Career Panel', 'Networking Event']
        for i in range(14, 21):
            option = self.data[f'Field{i}']
            if option != '':
                checkbox = QCheckBox(f"{option_list[14-i]}", self)
                checkbox.setChecked(True)
            else:
                checkbox = QCheckBox(f"{option_list[14-i]}", self)

            v_layout.addWidget(checkbox)
            checkbox.setEnabled(False)  # set all checkboxes uneditable

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
