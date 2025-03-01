from PySide6.QtWidgets import QDockWidget, QWidget, QVBoxLayout, QScrollArea, QSizePolicy
from PySide6.QtCore import Qt
from ui_ai_panel import Ui_DockWidget  # Импорт UI панели AI
from Ui_sceen import Ui_Frame  # Импорт UI сцены

class AiPanel(QDockWidget, Ui_DockWidget):
    """Панель инструментов AI с фиксированной шириной"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

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

        # Создаем новый UI_sceen
        new_sceen = QWidget(self)
        ui_sceen = Ui_Frame()
        ui_sceen.setupUi(new_sceen)

        # ✅ Подключаем кнопку `pen` к `open_drawing_settings`
        ui_sceen.pen.clicked.connect(self.parent().open_drawing_settings)

        # Устанавливаем заголовок сцены
        ui_sceen.groupBox_3.setTitle(f"Sceen {self.sceen_count}")

        # ✅ Настраиваем размер сцены, чтобы она не растягивалась
        new_sceen.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        # ✅ Добавляем сцену в layout
        self.sceen_layout.addWidget(new_sceen)

        # ✅ Обновляем размеры, чтобы scrollArea понимал, что контент увеличился
        self.scrollAreaWidgetContents.adjustSize()

