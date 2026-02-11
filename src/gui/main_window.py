import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  
        self.setWindowTitle("Image Converter")

        self.layout = QVBoxLayout()
        self.label = QLabel("Select an image to convert:")
        self.layout.addWidget(self.label)

        self.button = QPushButton("Choose File")
        self.button.clicked.connect(self.open_file_dialog)
        self.layout.addWidget(self.button)

        self.container = QWidget()  
        self.container.setLayout(self.layout)
        self.setCentralWidget(self.container)

    def open_file_dialog(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Image File", "", "Images (*.png *.xpm *.jpg *.tiff *.webp);;All Files (*)", options=options)
        if file_name:
            self.label.setText(f"Selected: {file_name}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())