from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QListWidget,
    QPushButton,
    QApplication,
    QListWidgetItem,
    QGridLayout,
    QVBoxLayout,
    QLayout,
    QLabel,
    QLineEdit,
    QCheckBox
)


class MainWindow(QWidget):
    def __init__(self, table_data):
        super().__init__()
        self.data = table_data
        self.full_record = None
        self.list_control: QListWidget = None
        self.prefix: QLineEdit = None
        self.first_name: QLineEdit = None
        self.last_name: QLineEdit = None
        self.title: QLineEdit = None
        self.org_name: QLineEdit = None
        self.email: QLineEdit = None
        self.org_website: QLineEdit = None
        self.phone: QLineEdit = None
        self.setup_ui()
        self.data_window = None

    def setup_ui(self):
        self.setWindowTitle("GUI")
        main_layout = QGridLayout()
        self.list_control = QListWidget()
        left_panel = QVBoxLayout()
        main_layout.addLayout(left_panel)
        left_panel.addWidget(self.list_control)
        right_panel = self.right_panel_frame()

        self.list_control.resize(400, 400)
        self.list_control.currentItemChanged.connect(self.demo_list_item_selected)
        self.put_data_in_list(self.data)

        quit_button = QPushButton("Quit Now")
        quit_button.clicked.connect(QApplication.instance().quit)
        quit_button.resize(quit_button.sizeHint())

        left_panel.addWidget(quit_button)
        main_layout.addLayout(right_panel)
        self.setLayout(main_layout)
        self.show()

    def right_panel_frame(self) -> QLayout:
        right_panel = QVBoxLayout()
        grid_layout = QGridLayout()
        right_panel.addLayout(grid_layout)

        grid_layout.addWidget(QLabel("Prefix"), 0, 0)
        self.prefix = QLineEdit()
        self.prefix.setReadOnly(True)
        grid_layout.addWidget(self.prefix, 0, 1)

        grid_layout.addWidget(QLabel("Name"), 0, 2)
        self.first_name = QLineEdit()
        self.first_name.setReadOnly(True)
        grid_layout.addWidget(self.first_name, 0, 3)
        self.last_name = QLineEdit()
        self.last_name.setReadOnly(True)
        grid_layout.addWidget(self.last_name, 0, 4)

        grid_layout.addWidget(QLabel("Title"), 0, 5)
        self.title = QLineEdit()
        self.title.setReadOnly(True)
        grid_layout.addWidget(self.title, 0, 6)

        grid_layout.addWidget(QLabel("Organization"), 1, 0)
        self.org_name = QLineEdit()
        self.org_name.setReadOnly(True)
        grid_layout.addWidget(self.org_name, 1, 1)

        grid_layout.addWidget(QLabel("Email"), 1, 2)
        self.email = QLineEdit()
        self.email.setReadOnly(True)
        grid_layout.addWidget(self.email, 1, 3)

        grid_layout.addWidget(QLabel("Website"), 1, 4)
        self.org_website = QLineEdit()
        self.org_website.setReadOnly(True)
        grid_layout.addWidget(self.org_website, 1, 5)

        grid_layout.addWidget(QLabel("Phone#"), 2, 0)
        self.phone = QLineEdit()
        self.phone.setReadOnly(True)
        grid_layout.addWidget(self.phone, 2, 1)

        return right_panel

    def put_data_in_list(self, data):
        for item in data:
            display_text = f"{item['Organization_Name']}"
            list_item = QListWidgetItem(display_text, listview=self.list_control)
            list_item.setData(1, item)

    def demo_list_item_selected(self, current: QListWidgetItem, previous: QListWidgetItem):
        selected_data = current.data(1)
        self.prefix.setText(selected_data["Prefix"])
        self.first_name.setText(selected_data["First_Name"])
        self.last_name.setText(selected_data["Last_Name"])
        self.title.setText(selected_data["Title"])
        self.org_name.setText(selected_data["Organization_Name"])
        self.email.setText(selected_data["Email"])
        self.org_website.setText(selected_data["Organization_Website"])
        self.phone.setText(selected_data["Phone"])
