from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QListWidget, QPushButton, QApplication, QListWidgetItem, QLabel, QLineEdit, \
    QVBoxLayout, QCheckBox, QHBoxLayout, QSplitter, QGridLayout

# import SecondWindow


class MainWindow(QWidget):
    def __init__(self, table_data):
        super().__init__()
        self.main_layout = None
        self.selected_list = None
        self.full_record = None
        self.data = table_data
        self.list_control = None
        self.setup_ui()
        self.checkbox = QCheckBox(self)
        # self.data_window = None
        # self.select_item_ui()

    def setup_ui(self):
        self.setWindowTitle("GUI")
        self.main_layout = QGridLayout(self)


        # Create the left side list widget
        display_list = QListWidget(self)
        self.list_control = display_list
        self.put_data_in_list(self.data)
        display_list.resize(400, 350)
        display_list.currentItemChanged.connect(self.demo_list_item_selected)

        # self.setGeometry(300, 300, 400, 500)
        self.main_layout.addWidget(display_list)

        quit_button = QPushButton("Quit Now", self)
        quit_button.clicked.connect(QApplication.instance().quit)
        quit_button.resize(quit_button.sizeHint())
        self.main_layout.addWidget(quit_button)
        # quit_button.move(300, 400)

        self.setGeometry(300, 300, 600, 500)
        self.show()

    def select_item_ui(self):
        label = QLabel(self)

        # for i in range(2, 13):
        #     option = self.data[f'Field{i}']
        #     if option != '':
        #         label.setText(option)

        # Prefix
        label.setText("Prefix:")
        display = QLineEdit(self.full_record['Field2'], self)
        display.setReadOnly(True)  # create QLineEdit uneditable
        self.main_layout.addWidget(label)
        self.main_layout.addWidget(display)

        # First Name
        label = QLabel("First Name:", self)
        display = QLineEdit(self.full_record['Field4'], self)
        display.setReadOnly(True)
        self.main_layout.addWidget(label)
        self.main_layout.addWidget(display)

        # Last Name
        label = QLabel("Last Name:", self)
        display = QLineEdit(self.full_record['Field5'], self)
        display.setReadOnly(True)
        self.main_layout.addWidget(label)
        self.main_layout.addWidget(display)

        # Title
        label = QLabel("Title:", self)
        display = QLineEdit(self.full_record['Field6'], self)
        display.setReadOnly(True)
        self.main_layout.addWidget(label)
        self.main_layout.addWidget(display)

        # Organization Name
        label = QLabel("Organization:", self)
        display = QLineEdit(self.full_record['Field7'], self)
        display.setReadOnly(True)
        self.main_layout.addWidget(label)
        self.main_layout.addWidget(display)

        # Email
        label = QLabel("Email:", self)
        display = QLineEdit(self.full_record['Field12'], self)
        display.setReadOnly(True)
        self.main_layout.addWidget(label)
        self.main_layout.addWidget(display)

        # Website
        label = QLabel("Website:", self)
        display = QLineEdit(self.full_record['Field9'], self)
        display.setReadOnly(True)
        self.main_layout.addWidget(label)
        self.main_layout.addWidget(display)

        # Phone Number
        label = QLabel("Phone#:", self)
        display = QLineEdit(self.full_record['Field10'], self)
        display.setReadOnly(True)
        self.main_layout.addWidget(label)
        self.main_layout.addWidget(display)

        # Intresting 1 - 7
        option_list = ['Course Project', 'Guest Speaker', 'Site Visit', 'Job Shadow', 'Internship', 'Career Panel',
                       'Networking Event']
        for i in range(14, 21):
            option = self.full_record[f'Field{i}']
            if option != '':
                self.checkbox = QCheckBox(f"{option_list[14 - i]}", self)
                self.checkbox.setChecked(True)
                self.checkbox.toggled.connect(self.prevent_toggle)
            else:
                self.checkbox = QCheckBox(f"{option_list[14 - i]}", self)
                self.checkbox.toggled.connect(self.prevent_toggle)

            self.main_layout.addWidget(self.checkbox)

        # Collaboration time period
        label = QLabel("Proposed collaboration time period")
        self.main_layout.addWidget(label)
        for i in range(114, 119):
            line = self.full_record[f'Field{i}']
            if line != '':
                display = QLineEdit(line, self)
                display.setReadOnly(True)
                self.main_layout.addWidget(display)

        # Description
        label = QLabel("CUBES Project Description")
        self.main_layout.addWidget(label)
        display = QLineEdit(self.full_record['Field214'], self)
        display.setReadOnly(True)
        self.main_layout.addWidget(display)

    def put_data_in_list(self, data: list[dict]):
        for item in data:
            display_text = f"{item['Field7']}"
            list_item = QListWidgetItem(display_text, listview=self.list_control)

    def find_full_data_record(self, org_name: str):
        for record in self.data:
            if record['Field7'] == org_name:
                return record

    # Maybe I need to set up another ui for display list item selected
    def demo_list_item_selected(self, current: QListWidgetItem, previous: QListWidgetItem):
        selected_data = current.data(0)
        self.full_record = self.find_full_data_record(selected_data)
        print(self.full_record)

        self.main_layout = QVBoxLayout(self)
        label = QLabel(self)

        # for i in range(2, 13):
        #     option = self.data[f'Field{i}']
        #     if option != '':
        #         label.setText(option)

        # Prefix
        label.setText("Prefix:")
        display = QLineEdit(self.full_record['Field2'], self)
        display.setReadOnly(True)  # create QLineEdit uneditable
        self.main_layout.addWidget(label)
        self.main_layout.addWidget(display)

        # First Name
        label = QLabel("First Name:", self)
        display = QLineEdit(self.full_record['Field4'], self)
        display.setReadOnly(True)
        self.main_layout.addWidget(label)
        self.main_layout.addWidget(display)

        # Last Name
        label = QLabel("Last Name:", self)
        display = QLineEdit(self.full_record['Field5'], self)
        display.setReadOnly(True)
        self.main_layout.addWidget(label)
        self.main_layout.addWidget(display)

        # Title
        label = QLabel("Title:", self)
        display = QLineEdit(self.full_record['Field6'], self)
        display.setReadOnly(True)
        self.main_layout.addWidget(label)
        self.main_layout.addWidget(display)

        # Organization Name
        label = QLabel("Organization:", self)
        display = QLineEdit(self.full_record['Field7'], self)
        display.setReadOnly(True)
        self.main_layout.addWidget(label)
        self.main_layout.addWidget(display)

        # Email
        label = QLabel("Email:", self)
        display = QLineEdit(self.full_record['Field12'], self)
        display.setReadOnly(True)
        self.main_layout.addWidget(label)
        self.main_layout.addWidget(display)

        # Website
        label = QLabel("Website:", self)
        display = QLineEdit(self.full_record['Field9'], self)
        display.setReadOnly(True)
        self.main_layout.addWidget(label)
        self.main_layout.addWidget(display)

        # Phone Number
        label = QLabel("Phone#:", self)
        display = QLineEdit(self.full_record['Field10'], self)
        display.setReadOnly(True)
        self.main_layout.addWidget(label)
        self.main_layout.addWidget(display)

        # Intresting 1 - 7
        option_list = ['Course Project', 'Guest Speaker', 'Site Visit', 'Job Shadow', 'Internship', 'Career Panel',
                       'Networking Event']
        for i in range(14, 21):
            option = self.full_record[f'Field{i}']
            if option != '':
                self.checkbox = QCheckBox(f"{option_list[14 - i]}", self)
                self.checkbox.setChecked(True)
                self.checkbox.toggled.connect(self.prevent_toggle)
            else:
                self.checkbox = QCheckBox(f"{option_list[14 - i]}", self)
                self.checkbox.toggled.connect(self.prevent_toggle)

            self.main_layout.addWidget(self.checkbox)

        # Collaboration time period
        label = QLabel("Proposed collaboration time period")
        self.main_layout.addWidget(label)
        for i in range(114, 119):
            line = self.full_record[f'Field{i}']
            if line != '':
                display = QLineEdit(line, self)
                display.setReadOnly(True)
                self.main_layout.addWidget(display)

        # Description
        label = QLabel("CUBES Project Description")
        self.main_layout.addWidget(label)
        display = QLineEdit(self.full_record['Field214'], self)
        display.setReadOnly(True)
        self.main_layout.addWidget(display)

        # self.data_window = SecondWindow.Comp490DataDemoWindow(full_record)
        # self.data_window.show()
        # self.clicked_data = full_record
        # print(self.clicked_data)

    def prevent_toggle(self):
        self.checkbox.setChecked(Qt.Checked)



