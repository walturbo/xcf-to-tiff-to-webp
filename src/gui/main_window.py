import sys
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QTabWidget, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QProgressBar, QLineEdit

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('XCF to TIFF to WebP Converter')
        self.setGeometry(100, 100, 600, 400)

        # Creating tabs
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        self.conversion_tab = QWidget()
        self.about_tab = QWidget()

        self.tabs.addTab(self.conversion_tab, 'Convert')
        self.tabs.addTab(self.about_tab, 'About')

        self.setup_conversion_tab()
        self.setup_about_tab()

    def setup_conversion_tab(self):
        layout = QVBoxLayout()

        self.file_path = QLineEdit()
        self.file_path.setPlaceholderText('Select XCF file')
        layout.addWidget(self.file_path)

        self.select_file_button = QPushButton('Browse')
        self.select_file_button.clicked.connect(self.select_file)
        layout.addWidget(self.select_file_button)

        self.quality_label = QLabel('Quality (1-100):')
        layout.addWidget(self.quality_label)

        self.quality_input = QLineEdit()
        self.quality_input.setPlaceholderText('Quality Setting')
        layout.addWidget(self.quality_input)

        self.convert_button = QPushButton('Convert to TIFF & WebP')
        self.convert_button.clicked.connect(self.convert_files)
        layout.addWidget(self.convert_button)

        self.progress_bar = QProgressBar()
        layout.addWidget(self.progress_bar)

        self.conversion_tab.setLayout(layout)

    def setup_about_tab(self):
        layout = QVBoxLayout()
        about_label = QLabel('XCF to TIFF to WebP Converter\nCreated by Walturbo\nDate: 2026-02-11')
        layout.addWidget(about_label)
        self.about_tab.setLayout(layout)

    def select_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Select XCF File", "", "XCF Files (*.xcf)")
        if file_name:
            self.file_path.setText(file_name)

    def convert_files(self):
        # Here you would implement the actual conversion logic
        self.progress_bar.setValue(0)  # Reset progress bar
        # Dummy progress loop
        for i in range(101):
            self.progress_bar.setValue(i)
            QtCore.QThread.msleep(50)  # Simulate time delay

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())