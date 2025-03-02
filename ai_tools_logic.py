from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtWidgets import QFrame
from PySide6.QtWidgets import QDockWidget, QWidget, QVBoxLayout, QScrollArea, QSizePolicy, QPushButton
from PySide6.QtCore import Qt
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

        # Создаём новый UI_sceen
        new_sceen = QWidget(self)
        ui_sceen = Ui_Frame()
        ui_sceen.setupUi(new_sceen)

        self.sceens.append(ui_sceen)

        parent_editor = self.parentWidget()
        if parent_editor:
            # ✅ Исправленный вызов `open_drawing_settings`
            ui_sceen.pen.clicked.connect(lambda _, btn=ui_sceen.pen: parent_editor.open_drawing_settings(btn))

        # ✅ Подключаем кнопку add_sub_sceen в момент создания сцены
        if hasattr(ui_sceen, "add_sub_sceen"):
            ui_sceen.add_sub_sceen.clicked.connect(lambda: self.add_new_sub_sceen(new_sceen))

        # Устанавливаем заголовок сцены
        ui_sceen.groupBox_3.setTitle(f"Sceen {self.sceen_count}")

        # ✅ Настраиваем размер сцены, чтобы она не растягивалась
        new_sceen.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        # ✅ Добавляем сцену в layout
        self.sceen_layout.addWidget(new_sceen)

        # ✅ Обновляем размеры, чтобы scrollArea понимал, что контент увеличился
        self.scrollAreaWidgetContents.adjustSize()

        hide_unhide_button = new_sceen.findChild(QPushButton, "hide_unhide")
        if hide_unhide_button:
            hide_unhide_button.clicked.connect(lambda: self.toggle_sub_sceen_visibility(new_sceen))
        else:
            print("Ошибка: Кнопка hide_unhide не найдена в сцене")

    def add_new_sub_sceen(self, parent_sceen):
        """Создаёт новую под-сцену и добавляет её внутрь scrollArea, расширяя его"""

        scroll_area = parent_sceen.findChild(QScrollArea, "scrollArea")
        if scroll_area is None:
            print("Ошибка: scrollArea не найден в parent_sceen")
            return

        new_sub_sceen = QWidget()  # Создаем под-сцену
        ui_new_sub_sceen = Ui_sub()
        ui_new_sub_sceen.setupUi(new_sub_sceen)

        if scroll_area.widget() is None:
            container = QWidget()
            layout = QVBoxLayout(container)
            layout.setSpacing(0)  # ✅ Убираем расстояния между sub_sceen
            layout.setContentsMargins(0, 0, 0, 0)  # ✅ Убираем отступы
            scroll_area.setWidget(container)
        else:
            container = scroll_area.widget()
            layout = container.layout()

        if layout is None:
            layout = QVBoxLayout()
            layout.setSpacing(0)  # ✅ Убираем расстояния между sub_sceen
            layout.setContentsMargins(0, 0, 0, 0)  # ✅ Убираем отступы
            container.setLayout(layout)

        layout.addWidget(new_sub_sceen)
        self.sceens.append(ui_new_sub_sceen)

        # ✅ Запрещаем прокрутку и увеличиваем высоту scrollArea
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll_area.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        scroll_area.setMinimumHeight(container.sizeHint().height())

        # ✅ Делаем groupBox_3 выше, чтобы вместить все sub_sceen
        parent_sceen.setMinimumHeight(parent_sceen.sizeHint().height() + new_sub_sceen.sizeHint().height())

        if hasattr(ui_new_sub_sceen, "pen"):
            parent_editor = self.parentWidget()
            if parent_editor:
                ui_new_sub_sceen.pen.clicked.connect(
                    lambda _, btn=ui_new_sub_sceen.pen: parent_editor.open_drawing_settings(btn))

        scroll_area.setWidget(container)
        self.scrollAreaWidgetContents.adjustSize()

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









