from PyQt6.QtWidgets import QTreeView
from PyQt6.QtGui import QFileSystemModel
import os

class FileViewer(QTreeView):
    def __init__(self):
        super().__init__()
        self.file_tree_model = QFileSystemModel()
        self.documents_path = os.path.expanduser("~/Documents/MEDLAB")
        self.file_tree_model.setRootPath(self.documents_path)
        self.setModel(self.file_tree_model)
        self.setRootIndex(self.file_tree_model.index(self.documents_path))