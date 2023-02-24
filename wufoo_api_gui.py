from PySide6.QtWidgets import QWidget, QListWidget, QPushButton, QApplication, QListWidgetItem, QLabel, QLineEdit, \
    QVBoxLayout, QCheckBox, QHBoxLayout, QSplitter

import SecondWindow


class MainWindow(QWidget):
    def __init__(self, table_data):
        super().__init__()
        self.data = table_data
        self.list_control = None
        self.clicked_data = table_data
        self.test = None
        self.setup_ui()
        # self.splliter()
        self.data_window = None
        # self.select_item_ui()

    def setup_ui(self):
        self.setWindowTitle("GUI")
        main_layout = QHBoxLayout(self)

        # Create the left side list widget
        display_list = QListWidget(self)
        self.list_control = display_list
        self.put_data_in_list(self.data)
        display_list.resize(400, 350)
        display_list.currentItemChanged.connect(self.demo_list_item_selected)
        # self.setGeometry(300, 300, 400, 500)
        main_layout.addWidget(display_list)

        # Create the right side layout
        right_layout = QVBoxLayout()
        main_layout.addLayout(right_layout)
        self.right_layout = right_layout

        quit_button = QPushButton("Quit Now", self)
        quit_button.clicked.connect(QApplication.instance().quit)
        quit_button.resize(quit_button.sizeHint())
        main_layout.addWidget(quit_button)
        # quit_button.move(300, 400)

        self.setGeometry(300, 300, 600, 500)
        self.show()

    def put_data_in_list(self, data: list[dict]):
        for item in data:
            # display_text = f"{item['Field7']}\t\t{item['Field4']}"
            display_text = f"{item['Field7']}"
            list_item = QListWidgetItem(display_text, listview=self.list_control)

    def find_full_data_record(self, orgName:str):
        for record in self.data:
            if record['Field7'] == orgName:
                return record

    def dict_contain_value(self, field:str, name:str):
        for value in self.data:
            if value[field] == name:
                self.test = value

    # Maybe I need to set up another ui for display list item selected
    def demo_list_item_selected(self, current: QListWidgetItem, previous: QListWidgetItem):
        selected_data = current.data(0)
        print(selected_data)
        full_record = self.find_full_data_record(selected_data)
        print(full_record)
        self.data_window = SecondWindow.Comp490DataDemoWindow(full_record)
        self.data_window.show()
        # self.clicked_data = full_record
        # print(self.clicked_data)


