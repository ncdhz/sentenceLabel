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

from PyQt5.QtWidgets import QWidget, QSplitter, QHBoxLayout
from PyQt5.QtCore import Qt
from sentenceLabelLib.LeftRightLabel import Label
from sentenceLabelLib.ScrollPanel import ScrollPanel

class MainPanel(QWidget):
    def __init__(self, parent, icon_path_left, icon_path_right, move_icon_path_left, move_icon_path_right):
        super(MainPanel, self).__init__()
        self.left_right = QSplitter(Qt.Orientation.Horizontal, self)
        self.top_bottom = QSplitter(Qt.Orientation.Vertical, self)

        self.left = Label(parent, icon_path_left, move_icon_path_left, True)   
        self.right = Label(parent, icon_path_right, move_icon_path_right)

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
