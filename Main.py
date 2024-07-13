import sys
import json
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QDialog, QLineEdit, QGraphicsColorizeEffect,
    QSizePolicy, QListWidget, QListWidgetItem, QWidget, QHBoxLayout, QLabel, QCheckBox, QVBoxLayout, QPushButton,
    QComboBox, QTabWidget, QVBoxLayout
)
from PySide6.QtCore import QPropertyAnimation, QRect, QEasingCurve, Qt, QTimer, QCoreApplication
from datetime import datetime

from Addwindow import *
from MainWindow import *


class CustomListItem(QWidget):
    def __init__(self, title, complexity, is_important):
        super().__init__()

        self.layout = QHBoxLayout(self)
        self.title_label = QLabel(title)
        self.title_label.setWordWrap(True)
        self.title_label.setMaximumWidth(200)

        self.complexity_label = QLabel(complexity)

        self.layout.addWidget(self.title_label)
        self.layout.addStretch()
        self.layout.addWidget(self.complexity_label)

        self.setLayout(self.layout)

        if is_important:
            self.setStyleSheet("QWidget  { border: 2px solid yellow; padding: 5px; }")
        else:
            self.setStyleSheet("QWidget { border: 0; padding: 5px; }")


class CustomTabWidget(QTabWidget):
    def __init__(self):
        super().__init__()
        self.setTabsClosable(True)
        self.tabCloseRequested.connect(self.remove_tab)

    def remove_tab(self, index):
        self.removeTab(index)


class Todo(QMainWindow):
    def __init__(self):
        super(Todo, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.menu_hidden = False
        self.ui.AddTB.clicked.connect(lambda: self.open_add_menu('todo'))
        self.ui.AddTB_2.clicked.connect(lambda: self.open_add_menu('inprogress'))
        self.ui.AddTB_3.clicked.connect(lambda: self.open_add_menu('done'))
        self.ui.Todobtn.clicked.connect(self.on_todobtn_clicked)
        self.ui.Inprogressbtn.clicked.connect(self.on_inprogressbtn_clicked)
        self.ui.Donebtn.clicked.connect(self.on_donebtn_clicked)
        self.ui.NotesBtn.clicked.connect(self.NotesBtn_clicked)
        self.ui.NotesAddBtn.clicked.connect(self.add_note)  # Add this line for the NotesAddBtn

        # Initialize clock update
        self.update_clock()
        self.setup_timer()

        # Load tasks from file
        self.load_tasks()

    def toggle_stat_menu(self):
        if self.ui.StatMenu.isVisible():
            self.ui.StatMenu.hide()
        else:
            self.ui.StatMenu.show()

    def open_add_menu(self, list_type):
        self.add_menu = AddMenu(self, list_type)
        self.add_menu.exec()

    def add_custom_item(self, title, complexity, is_important, save=True, list_widget=None):
        if not list_widget:
            list_widget = self.ui.TodoList_2

        item = QListWidgetItem(list_widget)
        custom_widget = CustomListItem(title, complexity, is_important)

        item.setSizeHint(custom_widget.sizeHint())
        list_widget.addItem(item)
        list_widget.setItemWidget(item, custom_widget)

        if save:
            self.save_tasks()

        self.update_task_count()

    def on_todobtn_clicked(self):
        self.animate_button(self.ui.Todobtn)

        if not self.menu_hidden:
            self.hide_window(self.ui.ToDoMenu)
        else:
            self.show_window(self.ui.ToDoMenu)

        self.menu_hidden = not self.menu_hidden

    def on_inprogressbtn_clicked(self):
        self.animate_button(self.ui.Inprogressbtn)

        if not self.menu_hidden:
            self.hide_window(self.ui.InProgressMenu)
        else:
            self.show_window(self.ui.InProgressMenu)

        self.menu_hidden = not self.menu_hidden

    def on_donebtn_clicked(self):
        self.animate_button(self.ui.Donebtn)

        if not self.menu_hidden:
            self.hide_window(self.ui.DoneMenu)
        else:
            self.show_window(self.ui.DoneMenu)

        self.menu_hidden = not self.menu_hidden

    def NotesBtn_clicked(self):
        self.animate_button(self.ui.NotesMain)

        if not self.menu_hidden:
            self.hide_notes_window(self.ui.NotesMain)
        else:
            self.show_notes_window(self.ui.NotesMain)

        self.menu_hidden = not self.menu_hidden

    def animate_button(self, button):
        color_effect = QGraphicsColorizeEffect(button)
        button.setGraphicsEffect(color_effect)

        self.color_animation = QPropertyAnimation(color_effect, b"strength")
        self.color_animation.setDuration(400)
        self.color_animation.setStartValue(0)
        self.color_animation.setKeyValueAt(0.5, 0.5)
        self.color_animation.setEndValue(0)
        self.color_animation.setEasingCurve(QEasingCurve.InOutCubic)
        self.color_animation.start()

    def hide_window(self, window):
        start_geometry = window.geometry()
        end_geometry = QRect(start_geometry.x(), start_geometry.y() - start_geometry.height(),
                             start_geometry.width(), start_geometry.height())

        self.menu_animation = QPropertyAnimation(window, b"geometry")
        self.menu_animation.setDuration(400)
        self.menu_animation.setStartValue(start_geometry)
        self.menu_animation.setEndValue(end_geometry)
        self.menu_animation.setEasingCurve(QEasingCurve.InOutQuad)
        self.menu_animation.finished.connect(lambda: window.hide())
        self.menu_animation.finished.connect(self.adjust_layout)
        self.menu_animation.start()

    def show_window(self, window):
        window.show()
        start_geometry = QRect(window.geometry().x(), window.geometry().y() - window.geometry().height(),
                               window.geometry().width(), window.geometry().height())
        end_geometry = window.geometry()

        self.menu_animation = QPropertyAnimation(window, b"geometry")
        self.menu_animation.setDuration(400)
        self.menu_animation.setStartValue(start_geometry)
        self.menu_animation.setEndValue(end_geometry)
        self.menu_animation.setEasingCurve(QEasingCurve.InOutQuad)
        self.menu_animation.finished.connect(self.adjust_layout)
        self.menu_animation.start()

    def show_notes_window(self, window):
        window.show()
        start_geometry = QRect(window.geometry().x() - window.geometry().width(), window.geometry().y(),
                               window.geometry().width(), window.geometry().height())
        end_geometry = window.geometry()

        self.notes_animation = QPropertyAnimation(window, b"geometry")
        self.notes_animation.setDuration(400)
        self.notes_animation.setStartValue(start_geometry)
        self.notes_animation.setEndValue(end_geometry)
        self.notes_animation.setEasingCurve(QEasingCurve.InOutQuad)
        self.notes_animation.finished.connect(self.adjust_layout)
        self.notes_animation.start()

    def hide_notes_window(self, window):
        start_geometry = window.geometry()
        end_geometry = QRect(start_geometry.x() - start_geometry.width(), start_geometry.y(),
                             start_geometry.width(), start_geometry.height())

        self.notes_animation = QPropertyAnimation(window, b"geometry")
        self.notes_animation.setDuration(400)
        self.notes_animation.setStartValue(start_geometry)
        self.notes_animation.setEndValue(end_geometry)
        self.notes_animation.setEasingCurve(QEasingCurve.InOutQuad)
        self.notes_animation.finished.connect(lambda: window.hide())
        self.notes_animation.finished.connect(self.adjust_layout)
        self.notes_animation.start()

    def adjust_layout(self):
        for i in range(self.ui.horizontalLayout.count()):
            widget = self.ui.horizontalLayout.itemAt(i).widget()
            widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            widget.updateGeometry()
        self.ui.centraMenu.updateGeometry()
        self.ui.UnderMenu.setFixedHeight(50)

    def update_clock(self):
        current_time = datetime.now().strftime("%d.%m.%Y %H:%M")
        self.ui.Clock.setText(QCoreApplication.translate("MainWindow", current_time, None))

    def setup_timer(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_clock)
        self.timer.start(1000)

    def save_tasks(self):
        tasks = {"todo": [], "inprogress": [], "done": []}
        for index in range(self.ui.TodoList_2.count()):
            item = self.ui.TodoList_2.item(index)
            custom_widget = self.ui.TodoList_2.itemWidget(item)
            task = {
                "title": custom_widget.title_label.text(),
                "complexity": custom_widget.complexity_label.text(),
                "is_important": "border: 2px solid yellow" in custom_widget.styleSheet()
            }
            tasks["todo"].append(task)

        for index in range(self.ui.InProgressList.count()):
            item = self.ui.InProgressList.item(index)
            custom_widget = self.ui.InProgressList.itemWidget(item)
            task = {
                "title": custom_widget.title_label.text(),
                "complexity": custom_widget.complexity_label.text(),
                "is_important": "border: 2px solid yellow" in custom_widget.styleSheet()
            }
            tasks["inprogress"].append(task)

        for index in range(self.ui.listWidget.count()):
            item = self.ui.listWidget.item(index)
            custom_widget = self.ui.listWidget.itemWidget(item)
            task = {
                "title": custom_widget.title_label.text(),
                "complexity": custom_widget.complexity_label.text(),
                "is_important": "border: 2px solid yellow" in custom_widget.styleSheet()
            }
            tasks["done"].append(task)

        with open("tasks.json", "w") as file:
            json.dump(tasks, file)

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as file:
                tasks = json.load(file)
                if isinstance(tasks, dict):
                    for task in tasks.get("todo", []):
                        self.add_custom_item(task["title"], task["complexity"], task["is_important"], save=False,
                                             list_widget=self.ui.TodoList_2)
                    for task in tasks.get("inprogress", []):
                        self.add_custom_item(task["title"], task["complexity"], task["is_important"], save=False,
                                             list_widget=self.ui.InProgressList)
                    for task in tasks.get("done", []):
                        self.add_custom_item(task["title"], task["complexity"], task["is_important"], save=False,
                                             list_widget=self.ui.listWidget)
                self.update_task_count()
        except FileNotFoundError:
            pass

    def update_task_count(self):
        todo_count = self.ui.TodoList_2.count()
        inprogress_count = self.ui.InProgressList.count()
        done_count = self.ui.listWidget.count()

        self.ui.ToDoText.setText(f"Tasks: {todo_count}")
        self.ui.InProgressText.setText(f"Tasks: {inprogress_count}")
        self.ui.DoneText.setText(f"Tasks: {done_count}")

    def add_note(self):
        new_tab_index = self.ui.NotesList.addTab(QWidget(), "New Note")
        self.ui.NotesList.setCurrentIndex(new_tab_index)


class AddMenu(QDialog):
    def __init__(self, parent=None, list_type='todo'):
        super(AddMenu, self).__init__(parent)
        self.ui = Ui_MainBody()
        self.ui.setupUi(self)
        self.ui.AddBtn.clicked.connect(self.add_click)
        self.parent_obj = parent
        self.list_type = list_type

        # Set fixed size
        self.setFixedSize(912, 64)

    def add_click(self):
        new_item_text = self.ui.TextInput.text()
        new_item_difficulty = self.ui.ChoseComplexity.currentText()
        is_important = self.ui.ImportantBtn.isChecked()

        if new_item_text and new_item_difficulty:
            if self.list_type == 'todo':
                self.parent_obj.add_custom_item(new_item_text, new_item_difficulty, is_important,
                                                list_widget=self.parent_obj.ui.TodoList_2)
            elif self.list_type == 'inprogress':
                self.parent_obj.add_custom_item(new_item_text, new_item_difficulty, is_important,
                                                list_widget=self.parent_obj.ui.InProgressList)
            elif self.list_type == 'done':
                self.parent_obj.add_custom_item(new_item_text, new_item_difficulty, is_important,
                                                list_widget=self.parent_obj.ui.listWidget)
        self.accept()

    def update_task_count(self):
        todo_count = self.ui.TodoList_2.count()
        inprogress_count = self.ui.InProgressList.count()
        done_count = self.ui.listWidget.count()

        self.ui.ToDoText.setText(f"Tasks: {todo_count}")
        self.ui.InProgressText.setText(f"Tasks: {inprogress_count}")
        self.ui.DoneText.setText(f"Tasks: {done_count}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Todo()
    window.show()
    sys.exit(app.exec())
