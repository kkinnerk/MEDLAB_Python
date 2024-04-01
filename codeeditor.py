from qtpy.Qsci import QsciScintilla
from qtpy.Qsci import QsciLexerPython

class CodeEditor(QsciScintilla):
    def __init__(self):
        super().__init__()
        self.lexer = QsciLexerPython()
        self.setLexer(self.lexer)