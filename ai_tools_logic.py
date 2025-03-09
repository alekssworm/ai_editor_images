from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtWidgets import QFrame
from PySide6.QtWidgets import QDockWidget, QWidget, QVBoxLayout, QScrollArea, QSizePolicy, QPushButton, QGraphicsItem, \
    QFileDialog
from PySide6.QtCore import Qt

from drawing_scene import DrawableObject
from ui_ai_panel import Ui_DockWidget  # Импорт UI панели AI
from Ui_sceen import Ui_Frame  # Импорт UI сцены
from sub_box import Ui_Frame as Ui_sub

class AiPanel(QDockWidget, Ui_DockWidget):
    """Панель инструментов AI с фиксированной шириной"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.sceens = []  # ✅ Список всех сцен

        # ✅ Устанавливаем минимальную ширину панели, чтобы она не была слишком узкой
        self.setMinimumWidth(300)  # Можно настроить ширину под ваш дизайн
        self.setMaximumWidth(500)  # Ограничение, если нужно

        # ✅ Настраиваем QScrollArea, чтобы он корректно изменял размер
        self.scrollArea.setMinimumWidth(280)  # Минимальная ширина для нормального отображения сцен
        self.scrollAreaWidgetContents.setMinimumWidth(280)

        # ✅ Создаем layout внутри scrollArea
        self.sceen_layout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.sceen_layout.setContentsMargins(0, 0, 0, 0)  # Убираем отступы контейнера
        self.sceen_layout.setAlignment(Qt.AlignTop)  # Выравниваем сцены к верху

        # ✅ Ограничиваем рост scrollAreaWidgetContents
        self.scrollAreaWidgetContents.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)

        # Счетчик сцен
        self.sceen_count = 0


        # Подключаем кнопку "add_sceen" к созданию новой сцены
        self.add_sceen.clicked.connect(self.add_new_sceen)

    def add_new_sceen(self):
        """Создаёт новую сцену и добавляет её внутрь QScrollArea"""
        self.sceen_count += 1  # Увеличиваем номер сцены

        new_sceen = QWidget(self)
        ui_sceen = Ui_Frame()
        ui_sceen.setupUi(new_sceen)

        # ✅ Подключаем кнопку render
        self.connect_render_button(ui_sceen, new_sceen)

        new_sceen.objects = []  # ✅ Добавляем список объектов
        self.sceens.append(new_sceen)

        parent_editor = self.parentWidget()
        if parent_editor:
            ui_sceen.pen.clicked.connect(
                lambda _, btn=ui_sceen.pen: parent_editor.open_drawing_settings(btn, new_sceen))

        if hasattr(ui_sceen, "add_sub_sceen"):
            ui_sceen.add_sub_sceen.clicked.connect(lambda: self.add_new_sub_sceen(new_sceen))

        # ✅ Подключаем удаление всей сцены
        if hasattr(ui_sceen, "trash"):
            ui_sceen.trash.clicked.connect(lambda: self.delete_sceen(new_sceen))

        ui_sceen.groupBox_3.setTitle(f"Sceen {self.sceen_count}")

        new_sceen.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self.sceen_layout.addWidget(new_sceen)

        self.scrollAreaWidgetContents.adjustSize()

        hide_unhide_button = new_sceen.findChild(QPushButton, "hide_unhide")
        if hide_unhide_button:
            hide_unhide_button.clicked.connect(lambda: self.toggle_sub_sceen_visibility(new_sceen))

    def add_new_sub_sceen(self, parent_sceen):
        """Создаёт новую под-сцену (sub_box) и добавляет её внутрь `sceen`"""

        scroll_area = parent_sceen.findChild(QScrollArea, "scrollArea")
        if scroll_area is None:
            print("Ошибка: scrollArea не найден в parent_sceen")
            return

        # ✅ Создаём sub_box
        new_sub_sceen = QWidget()
        ui_new_sub_sceen = Ui_sub()  # Загружаем UI sub_box (исправлено!)
        ui_new_sub_sceen.setupUi(new_sub_sceen)

        new_sub_sceen.objects = []  # ✅ Список объектов внутри sub_sceen
        parent_sceen.objects.append(new_sub_sceen)  # ✅ Связываем sub_sceen с sceen

        # ✅ Подключаем удаление sub_sceen через кнопку trash
        if hasattr(ui_new_sub_sceen, "trash"):
            ui_new_sub_sceen.trash.clicked.connect(lambda: self.delete_sub_sceen(parent_sceen, new_sub_sceen))

        # ✅ Добавляем sub_sceen в scrollArea
        if scroll_area.widget() is None:
            container = QWidget()
            layout = QVBoxLayout(container)
            layout.setSpacing(0)
            layout.setContentsMargins(0, 0, 0, 0)
            scroll_area.setWidget(container)
        else:
            container = scroll_area.widget()
            layout = container.layout()

        if layout is None:
            layout = QVBoxLayout()
            layout.setSpacing(0)
            layout.setContentsMargins(0, 0, 0, 0)
            container.setLayout(layout)

        layout.addWidget(new_sub_sceen)
        self.sceens.append(new_sub_sceen)  # ✅ Добавляем sub_sceen в список sceens

        # ✅ Обновляем параметры scrollArea
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll_area.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        scroll_area.setMinimumHeight(container.sizeHint().height())

        # ✅ Обновляем высоту sceen
        parent_sceen.setMinimumHeight(parent_sceen.sizeHint().height() + new_sub_sceen.sizeHint().height())

        # ✅ Подключаем `pen` для рисования в sub_sceen
        if hasattr(ui_new_sub_sceen, "pen"):
            parent_editor = self.parentWidget()
            if parent_editor:
                ui_new_sub_sceen.pen.clicked.connect(
                    lambda _, btn=ui_new_sub_sceen.pen: parent_editor.open_drawing_settings(btn, new_sub_sceen)
                )

        scroll_area.setWidget(container)
        self.scrollAreaWidgetContents.adjustSize()

    def delete_sceen(self, sceen):
        """Удаляет сцену, все её под-сцены, sub_box и нарисованные объекты"""

        # ✅ Удаляем все sub_sceen внутри sceen
        for sub_sceen in sceen.objects[:]:
            if isinstance(sub_sceen, QWidget):
                self.delete_sub_sceen(sceen, sub_sceen)

        # ✅ Удаляем все нарисованные объекты в sceen
        scene_view = self.parentWidget().graphicsView.scene()
        if hasattr(sceen, "objects"):
            for obj in sceen.objects[:]:
                if isinstance(obj, DrawableObject):  # 🔥 Удаляем DrawableObject
                    scene_view.removeItem(obj.item)
                    sceen.objects.remove(obj)

        # ✅ Удаляем sceen из списка
        if sceen in self.sceens:
            self.sceens.remove(sceen)

        # ✅ Удаляем sceen из интерфейса
        sceen.setParent(None)
        sceen.deleteLater()

        # ✅ Обновляем scrollArea
        self.scrollAreaWidgetContents.adjustSize()

    def delete_sub_sceen(self, parent_sceen, sub_sceen):
        """Удаляет под-сцену, sub_box и все её нарисованные элементы"""

        scene_view = self.parentWidget().graphicsView.scene()

        # ✅ Удаляем все нарисованные объекты sub_sceen
        if hasattr(sub_sceen, "objects"):
            for obj in sub_sceen.objects[:]:
                if isinstance(obj, DrawableObject):  # 🔥 Теперь удаляем DrawableObject
                    scene_view.removeItem(obj.item)
                    sub_sceen.objects.remove(obj)

        # ✅ Удаляем sub_sceen из родительского списка
        if sub_sceen in parent_sceen.objects:
            parent_sceen.objects.remove(sub_sceen)

        # ✅ Удаляем sub_sceen из интерфейса
        sub_sceen.setParent(None)
        sub_sceen.deleteLater()

        # ✅ Обновляем высоту parent_sceen
        parent_sceen.setMinimumHeight(parent_sceen.sizeHint().height())

        # ✅ Обновляем `scrollArea`
        scroll_area = parent_sceen.findChild(QScrollArea, "scrollArea")
        if scroll_area and scroll_area.widget():
            scroll_area.widget().adjustSize()

    def toggle_sub_sceen_visibility(self, parent_sceen):
        """Переключает видимость sub_sceen"""
        scroll_area = parent_sceen.findChild(QScrollArea, "scrollArea")
        if scroll_area is None:
            print("Ошибка: scrollArea не найден в parent_sceen")
            return

        if scroll_area.isVisible():
            scroll_area.hide()
        else:
            scroll_area.show()

    def connect_render_button(self, ui_sceen, sceen):
        """Подключает кнопку render к сохранению фигур"""
        if hasattr(ui_sceen, "render"):
            ui_sceen.render.clicked.connect(lambda: self.save_scene_shapes(sceen))

    def save_scene_shapes(self, sceen):
        """Сохраняет все фигуры из sceen и sub_sceen"""
        if not sceen:
            print("Ошибка: sceen не найден!")
            return

        save_folder = QFileDialog.getExistingDirectory(None, "Выберите папку для сохранения")
        if not save_folder:
            print("Ошибка: Папка не выбрана!")
            return

        # ✅ Сохраняем все фигуры из sceen
        self.parentWidget().graphicsView.scene().save_shapes_in_scene(sceen, save_folder)

        # ✅ Сохраняем все фигуры из sub_sceen
        for sub_sceen in sceen.objects:
            if isinstance(sub_sceen, QWidget) and hasattr(sub_sceen, "objects"):
                self.parentWidget().graphicsView.scene().save_shapes_in_scene(sub_sceen, save_folder)










