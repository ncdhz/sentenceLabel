from PyQt5.QtWidgets import QWidget, QSplitter, QHBoxLayout
from PyQt5.QtCore import Qt
from LeftRightLabel import Label
from ScrollPanel import ScrollPanel

class MainPanel(QWidget):
    def __init__(self, parent):
        super(MainPanel, self).__init__()
        self.left_right = QSplitter(Qt.Orientation.Horizontal, self)
        self.top_bottom = QSplitter(Qt.Orientation.Vertical, self)

        self.left = Label(parent, True)   
        self.right = Label(parent)

        self.sp_left = ScrollPanel(parent, ScrollPanel.Left)
        self.sp_top = ScrollPanel(parent, ScrollPanel.Top)
        self.sp_bottom = ScrollPanel(parent, ScrollPanel.Bottom)

        self.main_layout = QHBoxLayout(self)

        self.init_layout()
    
    def init_layout(self):
        
        self.sp_left.setMinimumSize(400, 450)
        self.sp_top.setMinimumSize(500, 300)
        self.sp_bottom.setMinimumSize(500, 150)
        self.left_right.addWidget(self.sp_left)
        self.top_bottom.addWidget(self.sp_top)
        self.top_bottom.addWidget(self.sp_bottom)
        self.left_right.addWidget(self.top_bottom)
        
        self.main_layout.addWidget(self.left)
        self.main_layout.addWidget(self.left_right)
        self.main_layout.addWidget(self.right)
        self.setLayout(self.main_layout)

    def refresh(self):
        self.sp_left.refresh()
        self.sp_top.refresh()
        self.sp_bottom.refresh()
