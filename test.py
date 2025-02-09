from PySide6.QtWidgets import QApplication, QTreeWidget, QTreeWidgetItem, QVBoxLayout, QPushButton, QWidget, QMenu
from PySide6.QtGui import QAction
from PySide6.QtCore import Qt  # ✅ Добавили импорт

class SceneEditor(QWidget):
    def __init__(self):
        super().__init__()

        self.tree = QTreeWidget()
        self.tree.setHeaderLabels(["Scenes and Objects"])
        self.tree.setContextMenuPolicy(Qt.CustomContextMenu)  # ✅ Теперь правильно
        self.tree.customContextMenuRequested.connect(self.show_context_menu)

        self.add_scene_button = QPushButton("+ Add Scene")
        self.add_scene_button.clicked.connect(self.add_scene)

        layout = QVBoxLayout()
        layout.addWidget(self.tree)
        layout.addWidget(self.add_scene_button)
        self.setLayout(layout)

    def add_scene(self, parent=None):
        """Добавление новой сцены"""
        if isinstance(parent, bool):  # Если parent оказался True/False, то заменяем его на None
            parent = None

        scene_name = f"Scene {self.tree.topLevelItemCount() + 1}" if parent is None else f"Sub-Scene {parent.childCount() + 1}"
        scene_item = QTreeWidgetItem([scene_name])

        if parent:
            parent.addChild(scene_item)
        else:
            self.tree.addTopLevelItem(scene_item)

    def add_object(self, parent):
        """Добавление объекта в сцену"""
        object_name = f"Object {parent.childCount() + 1}"
        object_item = QTreeWidgetItem([object_name])
        parent.addChild(object_item)

    def show_context_menu(self, position):
        """Контекстное меню при ПКМ"""
        item = self.tree.itemAt(position)
        if not item:
            return

        menu = QMenu()
        add_scene_action = QAction("Add Scene", self)
        add_object_action = QAction("Add Object", self)

        add_scene_action.triggered.connect(lambda: self.add_scene(item))
        add_object_action.triggered.connect(lambda: self.add_object(item))

        menu.addAction(add_scene_action)
        menu.addAction(add_object_action)
        menu.exec_(self.tree.viewport().mapToGlobal(position))

app = QApplication([])
window = SceneEditor()
window.show()
app.exec()
