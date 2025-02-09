from PySide6.QtWidgets import QFileDialog, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem
from PySide6.QtGui import QPixmap, QPainter
from PySide6.QtCore import Qt


class ImageViewer(QGraphicsView):
    """Класс для отображения и масштабирования изображения"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setScene(QGraphicsScene(self))  # Создаем сцену
        self.image_item = QGraphicsPixmapItem()  # Объект для изображения
        self.scene().addItem(self.image_item)
        self.setRenderHint(QPainter.Antialiasing)
        self.scale_factor = 1.0  # Начальный масштаб

    def set_image(self, file_path):
        """Загружает и отображает изображение без растяжения"""
        pixmap = QPixmap(file_path)
        self.image_item.setPixmap(pixmap)
        self.scene().setSceneRect(pixmap.rect())  # Размер сцены = размер изображения

    def wheelEvent(self, event):
        """Обработчик колесика мыши для масштабирования"""
        zoom_in_factor = 1.25
        zoom_out_factor = 0.8
        if event.angleDelta().y() > 0:
            self.scale(zoom_in_factor, zoom_in_factor)
            self.scale_factor *= zoom_in_factor
        else:
            self.scale(zoom_out_factor, zoom_out_factor)
            self.scale_factor *= zoom_out_factor


def import_image(image_viewer):
    """Открывает файловый диалог и загружает изображение в ImageViewer"""
    file_path, _ = QFileDialog.getOpenFileName(None, "Выбрать изображение", "", "Images (*.png *.jpg *.jpeg *.bmp)")
    if file_path:
        image_viewer.set_image(file_path)  # Отображаем изображение
