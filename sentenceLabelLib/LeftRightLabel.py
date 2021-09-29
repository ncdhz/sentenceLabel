# Copyright 2021 ncdhz

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QWidget, QVBoxLayout
class Label(QWidget):
    def __init__(self, parent, icon_path, move_icon_path, left = False):
        super(Label, self).__init__()
        self.setMouseTracking(True)
        self.label = QLabel()
        self.v_layout = QVBoxLayout() 
        self.left = left
        self.pt = parent
        self.icon_path = icon_path
        self.move_icon_path = move_icon_path
        self.init_layout()
     
    def init_layout(self):
        self.label.setPixmap(QPixmap(self.icon_path))
        self.v_layout.addWidget(self.label)
        self.setLayout(self.v_layout)
    
    def mouseReleaseEvent(self, ev):
        self.pt.move_func(self.left)
    
    def mouseMoveEvent(self, QMouseEvent):
        self.label.setStyleSheet('background:#dbdbdb;')
        self.label.setPixmap(QPixmap(self.move_icon_path))

    def leaveEvent(self, QMouseEvent):
        self.label.setStyleSheet('background:rgba(0,0,0,0);')
        self.label.setPixmap(QPixmap(self.icon_path))
