from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QWidget, QVBoxLayout
class Label(QWidget):
    def __init__(self, parent, left = False):
        super(Label, self).__init__()
        self.setMouseTracking(True)
        self.label = QLabel()
        self.v_layout = QVBoxLayout() 
        self.left = left
        self.pt = parent
        self.init_layout()
     
    def init_layout(self):
        if self.left:
            self.label.setPixmap(QPixmap('images/left.png'))
        else:
            self.label.setPixmap(QPixmap('images/right.png'))
        self.v_layout.addWidget(self.label)
        self.setLayout(self.v_layout)
    
    def mouseReleaseEvent(self, ev):
        self.pt.move_func(self.left)
            
                
        
    def mouseMoveEvent(self, QMouseEvent):
        self.label.setStyleSheet('background:#dbdbdb;')
        if self.left:
            self.label.setPixmap(QPixmap('images/move-left.png'))
        else:
            self.label.setPixmap(QPixmap('images/move-right.png'))

    def leaveEvent(self, QMouseEvent):
        self.label.setStyleSheet('background:rgba(0,0,0,0);')
        if self.left:
            self.label.setPixmap(QPixmap('images/left.png'))
        else:
            self.label.setPixmap(QPixmap('images/right.png'))
