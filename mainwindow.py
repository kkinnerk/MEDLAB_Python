from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QMenuBar, QFileDialog, QTabWidget, QHBoxLayout
from PyQt6.QtGui import QAction
from fileviewer import FileViewer
from codeeditor import CodeEditor
from console import Console

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MedLab Operation Environment (Beta 0.1)")
        self.setGeometry(100, 100, 900, 900)
        self.initui()
        self.new_document()

    def initui(self):
        self.create_menubar()

        central_widget = QWidget()
        horizontal_layout = QHBoxLayout(central_widget)

        self.file_viewer = FileViewer()
        horizontal_layout.addWidget(self.file_viewer)

        right_widget = QWidget()
        vertical_layout = QVBoxLayout(right_widget)

        self.editor_tabs = QTabWidget()
        self.editor_tabs.setTabsClosable(True)
        self.editor_tabs.tabCloseRequested.connect(self.close_tab)
        vertical_layout.addWidget(self.editor_tabs)

        self.console = Console()
        vertical_layout.addWidget(self.console)

        horizontal_layout.addWidget(right_widget)

        self.setCentralWidget(central_widget)

    def create_menubar(self):
        menubar = QMenuBar()
        file_menu = menubar.addMenu("File")

        new_action = QAction("New", self)
        new_action.triggered.connect(self.new_document)
        file_menu.addAction(new_action)

        open_action = QAction("Open", self)
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)

        save_action = QAction("Save", self)
        save_action.triggered.connect(self.save_file)
        file_menu.addAction(save_action)

        run_action = QAction("Run", self)
        run_action.triggered.connect(self.execute_code)
        file_menu.addAction(run_action)

        self.setMenuBar(menubar)

    def new_document(self):
        new_editor = CodeEditor()
        tab_index = self.editor_tabs.addTab(new_editor, f"Untitled-{self.editor_tabs.count() + 1}")
        self.editor_tabs.setCurrentIndex(tab_index)

    def close_tab(self, index):
        self.editor_tabs.removeTab(index)

    def execute_code(self):
        current_editor = self.editor_tabs.currentWidget()
        if current_editor:
            self.code = current_editor.text()
            self.console.execute(self.code)

    def save_file(self):
        current_editor = self.editor_tabs.currentWidget()
        if current_editor:
            filename, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Python Files (*.py)")
            if filename:
                with open(filename, 'w') as file:
                    file.write(current_editor.text())
                self.editor_tabs.setTabText(self.editor_tabs.currentIndex(), filename.split('/')[-1])

    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Python Files (*.py)")
        if filename:
            with open(filename, 'r') as file:
                content = file.read()
            new_editor = CodeEditor()
            new_editor.setText(content)  # Corrected this line
            tab_index = self.editor_tabs.addTab(new_editor, filename.split('/')[-1])
            self.editor_tabs.setCurrentIndex(tab_index)
