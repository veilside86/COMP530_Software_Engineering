import wufoo_api as wa

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
    QHBoxLayout,
    QCheckBox,
    QMessageBox,
    QStackedWidget
)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.data = MainWindow.get_data_from_server()
        self.central_widget: QStackedWidget = None
        self.list_control: QListWidget = None
        self.prefix: QLineEdit = None
        self.first_name: QLineEdit = None
        self.last_name: QLineEdit = None
        self.title: QLineEdit = None
        self.org_name: QLineEdit = None
        self.email: QLineEdit = None
        self.org_website: QLineEdit = None
        self.phone: QLineEdit = None
        self.course_project: QCheckBox = None
        self.guest_speaker: QCheckBox = None
        self.site_visit: QCheckBox = None
        self.job_shadow: QCheckBox = None
        self.internship: QCheckBox = None
        self.career_panel: QCheckBox = None
        self.networking_event: QCheckBox = None
        self.collaboration_time: QLineEdit = None
        self.permission: QLineEdit = None
        self.msg_box: QMessageBox = None
        self.data_visualization_ui()

    def data_visualization_ui(self):
        self.setWindowTitle("CUBES Project")
        main_layout = QHBoxLayout()
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

        grid_layout.addWidget(QLabel("Title"), 1, 0)
        self.title = QLineEdit()
        self.title.setReadOnly(True)
        grid_layout.addWidget(self.title, 1, 1)

        grid_layout.addWidget(QLabel("Organization"), 1, 2)
        self.org_name = QLineEdit()
        self.org_name.setReadOnly(True)
        grid_layout.addWidget(self.org_name, 1, 3)

        grid_layout.addWidget(QLabel("Email"), 2, 0)
        self.email = QLineEdit()
        self.email.setReadOnly(True)
        grid_layout.addWidget(self.email, 2, 1, 1, 2)

        grid_layout.addWidget(QLabel("Website"), 3, 0)
        self.org_website = QLineEdit()
        self.org_website.setReadOnly(True)
        grid_layout.addWidget(self.org_website, 3, 1, 1, 2)

        self.course_project = QCheckBox("Course Project")
        self.course_project.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.course_project.setFocusPolicy(Qt.NoFocus)
        grid_layout.addWidget(self.course_project, 4, 0)

        self.guest_speaker = QCheckBox("Guest Speaker")
        self.guest_speaker.setAttribute(Qt.WA_TransparentForMouseEvents)
        grid_layout.addWidget(self.guest_speaker, 4, 1)
        self.site_visit = QCheckBox("Site Visit")
        self.site_visit.setAttribute(Qt.WA_TransparentForMouseEvents)
        grid_layout.addWidget(self.site_visit, 4, 2)
        self.job_shadow = QCheckBox("Job Shadow")
        self.job_shadow.setAttribute(Qt.WA_TransparentForMouseEvents)
        grid_layout.addWidget(self.job_shadow, 4, 3)
        self.internship = QCheckBox("Internship")
        self.internship.setAttribute(Qt.WA_TransparentForMouseEvents)
        grid_layout.addWidget(self.internship, 4, 4)
        self.career_panel = QCheckBox("Career Panel")
        self.career_panel.setAttribute(Qt.WA_TransparentForMouseEvents)
        grid_layout.addWidget(self.career_panel, 4, 5)
        self.networking_event = QCheckBox("Networking Event")
        self.networking_event.setAttribute(Qt.WA_TransparentForMouseEvents)
        grid_layout.addWidget(self.networking_event, 4, 6)

        grid_layout.addWidget(QLabel("Collaboration Time Period"), 5, 0)
        self.collaboration_time = QLineEdit()
        self.collaboration_time.setReadOnly(True)
        grid_layout.addWidget(self.collaboration_time, 5, 1, 1, 3)

        grid_layout.addWidget(QLabel("CUBES Project Permission"), 6, 0)
        self.permission = QLineEdit()
        self.permission.setReadOnly(True)
        grid_layout.addWidget(self.permission, 6, 1, 1, 2)

        return right_panel

    def put_data_in_list(self, data):
        for item in data:
            display_text = f"{item['Organization_Name']}"
            list_item = QListWidgetItem(display_text, listview=self.list_control)
            list_item.setData(1, item)

    def data_update(self):
        self.msg_box = QMessageBox()
        self.msg_box.setWindowTitle("Alert")
        self.msg_box.setText("Data Updated")
        self.msg_box.exec_()

    def refresh(self):
        self.central_widget.setCurrentWidget(self.data_visualization_ui)

    def demo_list_item_selected(self, current: QListWidgetItem, previous: QListWidgetItem):
        selected_data = current.data(1)
        self.prefix.setText(selected_data["Prefix"])
        self.first_name.setText(selected_data["First_Name"])
        self.last_name.setText(selected_data["Last_Name"])
        self.title.setText(selected_data["Title"])
        self.org_name.setText(selected_data["Organization_Name"])
        self.email.setText(selected_data["Email"])
        self.org_website.setText(selected_data["Organization_Website"])
        self.course_project.setChecked(bool(selected_data["Interested_Opt1"]))
        self.guest_speaker.setChecked(bool(selected_data["Interested_Opt2"]))
        self.site_visit.setChecked(bool(selected_data["Interested_Opt3"]))
        self.job_shadow.setChecked(bool(selected_data["Interested_Opt4"]))
        self.internship.setChecked(bool(selected_data["Interested_Opt5"]))
        self.career_panel.setChecked(bool(selected_data["Interested_Opt6"]))
        self.networking_event.setChecked(bool(selected_data["Interested_Opt7"]))

        for i in range(1, 6):
            line = selected_data[f'Collabo_Time_Opt{i}']
            if line != '':
                self.collaboration_time.setText(selected_data[f'Collabo_Time_Opt{i}'])

        self.permission.setText(selected_data["Permission"])

    @staticmethod
    def get_data_from_server():
        conn, cursor = wa.open_db()
        cursor.execute('''SELECT * FROM wufoo''')
        column_headers = [i[0] for i in cursor.description]
        all_data = cursor.fetchall()

        # data with column names
        db_data = []
        for row in all_data:
            rows = {}
            for i in range(len(column_headers)):
                rows[column_headers[i]] = row[i]
            db_data.append(rows)

        return db_data
