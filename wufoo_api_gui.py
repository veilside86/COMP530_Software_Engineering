from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QListWidget, QPushButton, QApplication, QListWidgetItem, QLabel, QLineEdit, \
    QVBoxLayout, QCheckBox, QHBoxLayout, QSplitter, QGridLayout

import SecondWindow


class MainWindow(QWidget):
    def __init__(self, table_data):
        super().__init__()
        self.main_layout = None
        self.selected_list = None
        self.full_record = None
        self.data = table_data
        self.list_control = None
        self.setup_ui()
        # self.checkbox = QCheckBox(self)
        self.data_window = None
        # self.select_item_ui()

    def setup_ui(self):
        self.setWindowTitle("GUI")
        self.main_layout = QGridLayout(self)
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

        self.setGeometry(300, 300, 300, 500)
        self.show()

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
        # print(self.full_record)
        self.data_window = SecondWindow.Comp490DataDemoWindow(self.full_record)
        self.data_window.show()
