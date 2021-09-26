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

import sys
from PyQt5.QtGui import QDesktopServices, QIcon
from PyQt5.QtWidgets import QApplication, QInputDialog, QMainWindow, QAction, QFileDialog, QMessageBox
from PyQt5.QtCore import QMimeData, QUrl
from sentenceLabelLib.MainPanel import MainPanel
import json
from sentenceLabelLib.resources import *
from sentenceLabelLib.utils import Tools
from sentenceLabelLib import utils

class MainWindow(QMainWindow):
    
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.setMinimumSize(1100, 600)
        self.edit_data = None
        self.start = 0
        self.end = 0
        self.middle = 0
        self.is_save = True
        self.file = ''
        self.segmentation = ''
        self.file_menu = self.menuBar().addMenu('File')
        self.edit_menu = self.menuBar().addMenu('Edit')
        self.help_menu = self.menuBar().addMenu('Help')

        self.file_toolbar = self.addToolBar('File')
        self.edit_toolbar = self.addToolBar('Edit')

        self.status_bar = self.statusBar()

        self.open_action = QAction('Open', self)
        self.save_action = QAction('Save', self)
        self.save_as_action = QAction('Save As', self)
        self.close_action = QAction('Close', self)
        
        self.copy_action = QAction('Copy', self)
        self.paste_action = QAction('Paste', self)
        self.left_action = QAction('Left', self)
        self.right_action = QAction('Right', self)
        self.jump_action = QAction('Jump', self)
        self.delete_current_action = QAction('Delete current', self)
        self.delete_all_action = QAction('Delete all', self)

        self.document_action = QAction('Document', self)
        self.main_panel = MainPanel(self, ':/left', ':/right', ':/move-left', ':/move-right')
        self.setWindowIcon(QIcon(':/logo'))
        self.setCentralWidget(self.main_panel)
        self.menu_init()
        self.toolbar_init()
        self.status_bar_init()
        self.action_init()
    
    def menu_init(self):
        self.file_menu.addAction(self.open_action)
        self.file_menu.addAction(self.save_action)
        self.file_menu.addAction(self.save_as_action)
        self.file_menu.addSeparator()
        self.file_menu.addAction(self.close_action)

        self.edit_menu.addAction(self.copy_action)
        self.edit_menu.addAction(self.paste_action)
        self.edit_menu.addSeparator()
        self.edit_menu.addAction(self.left_action)
        self.edit_menu.addAction(self.right_action)
        self.edit_menu.addAction(self.jump_action)
        self.edit_menu.addSeparator()
        self.edit_menu.addAction(self.delete_current_action)
        self.edit_menu.addAction(self.delete_all_action)

        self.help_menu.addAction(self.document_action)

    def toolbar_init(self):
        self.file_toolbar.addAction(self.open_action)
        self.file_toolbar.addAction(self.save_action)
        self.file_toolbar.addAction(self.save_as_action)
        self.file_toolbar.addAction(self.close_action)

        self.edit_toolbar.addAction(self.left_action)
        self.edit_toolbar.addAction(self.right_action)
        self.edit_toolbar.addAction(self.jump_action)
        self.edit_toolbar.addAction(self.delete_current_action)
        self.edit_toolbar.addAction(self.delete_all_action)
        self.edit_toolbar.addAction(self.copy_action)
        self.edit_toolbar.addAction(self.paste_action)
        self.edit_toolbar.addAction(self.document_action)

    def status_bar_init(self):
        self.status_bar.showMessage('Ready Go !!!')
    
    def action_init(self):
        self.open_action.setIcon(QIcon(':/open'))
        self.open_action.setShortcut('Ctrl+O')
        self.open_action.setToolTip('Open an existing file')
        self.open_action.setStatusTip('Open an existing file')
        self.open_action.triggered.connect(self.open_func)

        self.save_action.setIcon(QIcon(':/save'))
        self.save_action.setShortcut('Ctrl+S')
        self.save_action.setToolTip('Save the file')
        self.save_action.setStatusTip('Save the file')
        self.save_action.triggered.connect(self.save_func)

        self.save_as_action.setIcon(QIcon(':/save-as'))
        self.save_as_action.setShortcut('Ctrl+A')
        self.save_as_action.setToolTip('Save the file to a specified location')
        self.save_as_action.setStatusTip('Save the file to a specified location')
        self.save_as_action.triggered.connect(self.save_as_func)

        self.close_action.setIcon(QIcon(':/close'))
        self.close_action.setShortcut('Ctrl+E')
        self.close_action.setToolTip('Close the file')
        self.close_action.setStatusTip('Close the file')
        self.close_action.triggered.connect(self.close_func)


        self.left_action.setIcon(QIcon(':/xiangzuo'))
        self.left_action.setShortcut('A')
        self.left_action.setToolTip('Towards the left')
        self.left_action.setStatusTip('Towards the left')
        self.left_action.triggered.connect(self.left_func)

        self.right_action.setIcon(QIcon(':/xiangyou'))
        self.right_action.setShortcut('D')
        self.right_action.setToolTip('Towards the right')
        self.right_action.setStatusTip('Towards the right')
        self.right_action.triggered.connect(self.right_func)

        self.jump_action.setIcon(QIcon(':/jump'))
        self.jump_action.setShortcut('Ctrl+J')
        self.jump_action.setToolTip('Move to specified article')
        self.jump_action.setStatusTip('Move to specified article')
        self.jump_action.triggered.connect(self.jump_func)

        self.delete_current_action.setIcon(QIcon(':/d1'))
        self.delete_current_action.setToolTip('Delete current labels')
        self.delete_current_action.setStatusTip('Delete current labels')
        self.delete_current_action.triggered.connect(self.delete_current_func)

        self.delete_all_action.setIcon(QIcon(':/d2'))
        self.delete_all_action.setToolTip('Delete all labels')
        self.delete_all_action.setStatusTip('Delete all labels')
        self.delete_all_action.triggered.connect(self.delete_all_func)

        self.copy_action.setIcon(QIcon(':/copy'))
        self.copy_action.setShortcut('Ctrl+C')
        self.copy_action.setToolTip('Copy the text')
        self.copy_action.setStatusTip('Copy the text')
        self.copy_action.triggered.connect(self.copy_func)

        self.paste_action.setIcon(QIcon(':/paste'))
        self.paste_action.setShortcut('Ctrl+V')
        self.paste_action.setToolTip('Paste the text')
        self.paste_action.setStatusTip('Paste the text')
        self.paste_action.triggered.connect(self.paste_func)

        self.document_action.setIcon(QIcon(':/document'))
        self.document_action.setShortcut('Ctrl+D')
        self.document_action.setToolTip('Open the document')
        self.document_action.setStatusTip('Open the document')
        self.document_action.triggered.connect(self.document_func)

        self.mime_data = QMimeData()
        self.clipboard = QApplication.clipboard()

    def delete_current_func(self):
        if self.edit_data:
            self.is_save = False
            self.edit_data[Tools.Data][self.middle][Tools.Sentences] = []
            self.edit_data[Tools.Data][self.middle][Tools.Number] = 0
            self.main_panel.refresh()
    
    def delete_all_func(self):
        if self.edit_data:
            delete = QMessageBox.information(self, 'Delete', 'Is it delete all labels?', QMessageBox.Yes | QMessageBox.No)
            if delete == QMessageBox.Yes:
                self.is_save = False
                for i in range(self.end):
                    self.edit_data[Tools.Data][i][Tools.Sentences] = []
                    self.edit_data[Tools.Data][i][Tools.Number] = 0
                self.main_panel.refresh()

    def closeEvent(self, event):
        save = self.save_file()
        if save == QMessageBox.Yes or save == QMessageBox.No:
            event.accept()
        else:
            event.ignore()

    def save_func(self):
        if not self.file:
            self.save_as_func()
            return
        if not self.edit_data:
            QMessageBox.information(self, 'Save', 'File not open!!!', QMessageBox.Yes)
            return
        with open(self.file, 'w', encoding='utf-8') as f:
            json.dump(self.edit_data, f, indent=4, ensure_ascii=False)
        self.is_save = True

    def save_as_func(self):
        if not self.edit_data:
            QMessageBox.information(self, 'Save', 'File not open!!!', QMessageBox.Yes)
            return
        file = QFileDialog.getSaveFileName(self, 'Save File', './', 'Files (*.json *.txt)')
        if file[0]:
            with open(file[0], 'w', encoding='utf-8') as f:
                json.dump(self.edit_data, f, indent=4, ensure_ascii=False)
            self.file = file[0]
            self.is_save = True

    def close_func(self):
        save = self.save_file()
        if save == QMessageBox.Yes or save == QMessageBox.No:
            self.middle = 0
            self.start = 0
            self.end = 0
            self.edit_data = None
            self.file = ''
            self.is_save = True
            self.segmentation = ''
            self.main_panel.refresh()
            utils.refresh()
        
        return save

    def save_file(self):
        if not self.is_save:
            save = QMessageBox.information(self, 'Save', 'Whether to save changes?', QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
            if save == QMessageBox.Yes:
                with open(self.file, 'w', encoding='utf-8') as f:
                    json.dump(self.edit_data, f, indent=4, ensure_ascii=False)
                self.is_save = True
            return save
        return QMessageBox.Yes

    def left_func(self):
        self.move_func(True)

    def right_func(self):
        self.move_func(False)
    
    def item_is_save(self, d):
        self.is_save = False
        ss = self.edit_data[Tools.Data][self.middle].get(Tools.Sentences, [])
        is_save = True
        if d in ss: 
            ss.remove(d)
        else:
            ss.append(d)
            is_save = False
        self.edit_data[Tools.Data][self.middle][Tools.Sentences] = ss
        self.edit_data[Tools.Data][self.middle][Tools.Number] = len(ss)
        return is_save
        
    def move_func(self, left=False):
        if self.edit_data:
            if left:
                if self.middle - 1 < self.start:
                    QMessageBox.information(self, '', 
                f'''There is no data ahead!!!''', QMessageBox.StandardButton.Ok)
                else:
                    self.middle -= 1
                    self.main_panel.refresh()
            else:
                if self.middle + 1 >= self.end:
                    QMessageBox.information(self, '', 
                f'''There is no data behind!!!''', QMessageBox.StandardButton.Ok)
                else:
                    self.middle += 1
                    self.main_panel.refresh()

    def jump_func(self):
        if not self.edit_data:
            QMessageBox.information(self, 'Jump', 'File not open!!!', QMessageBox.Yes)
            return
        number, ok = QInputDialog.getInt(self, 'Number of articles', 'Please enter the number of articles:')
        if ok:
            if number < self.start:
                QMessageBox.information(self, 'Jump', 'The number is too small!!!', QMessageBox.Yes)
            elif number >= self.end:
                QMessageBox.information(self, 'Jump', 'The number is too large!!!', QMessageBox.Yes)
            else:
                self.middle = number
                self.main_panel.refresh()

    def copy_func(self):
        if not self.edit_data:
            QMessageBox.information(self, 'Copy', 'File not open!!!', QMessageBox.Yes)
            return
        self.mime_data.setText(json.dumps(self.edit_data[Tools.Data][self.middle], indent=4))
        self.clipboard.setMimeData(self.mime_data)
    
    def paste_func(self):
        d = self.clipboard.mimeData().text()
        try:
            jd = json.loads(d)
            utils.check_format(jd)
            if self.edit_data:
                self.edit_data[Tools.Data].install(self.middle, jd)
            else:
                self.edit_data = {
                    Tools.Data: [jd]
                }
                self.segmentation = self.edit_data.get(Tools.Segmentation, utils.SegmentationFunc())
            self.end += 1
            self.is_save = False 
            self.main_panel.refresh()
        except:
            self.data_format_error(is_data=True)


    def document_func(self):
        QDesktopServices.openUrl(QUrl('http://www.myhwx.com/sentence-label'))

    def open_func(self):
        file, _ = QFileDialog.getOpenFileName(self, 'Open File', './', 'Files (*.txt *.json)')
        if file:
            cf = self.close_func()
            if cf == QMessageBox.Cancel:
                return
            try:
                with open(file, 'r', encoding='utf-8') as f:
                    self.edit_data = json.load(f)

                config = self.edit_data.get(Tools.Config, {})

                is_config = utils.injection(config)

                if not is_config:
                    self.config_format_error()
                    return
                try:
                    if Tools.Segmentation in self.edit_data and Tools.SentName in self.edit_data:
                        sn = self.edit_data[Tools.SentName]
                        assert type(sn) == str
                        assert len(sn) >= 1
                        for s_ in sn:
                            assert (s_.lower() <= 'z' and s_.lower() >= 'a') or s_.lower() == '_'
                        Tools.SentList = self.edit_data[Tools.SentName]
                except Exception:
                    QMessageBox.critical(self, 'Variable name Error', f'''<pre>Variable name Error:<p style="color:rgba(255, 0, 0, 0.8)">[sentName] is a variable name</p></pre>''', QMessageBox.StandardButton.Ok)
                    utils.refresh()
                    return
                try:
                    # 动态定义切分文章问方法的函数
                    self.segmentation = self.edit_data.get(Tools.Segmentation, utils.SegmentationFunc())
                    utils.check_segmentation(self.segmentation)
                except Exception:
                    QMessageBox.critical(self, 'Segmentation Error', f'''<pre>Segmentation Error:<p style="color:rgba(255, 0, 0, 0.8)">input: article<br/>output:{Tools.SentList}<br/>{Tools.SentList}: a string list<br/></p></pre>''', QMessageBox.StandardButton.Ok)
                    utils.refresh()
                    self.segmentation = ''
                    return

                for d in self.edit_data[Tools.Data]:
                    utils.check_format(d)
                self.end = len(self.edit_data[Tools.Data])
                self.start = 0
                self.middle = 0
                self.file = file
                self.main_panel.refresh()
            except Exception as ex:
                self.data_format_error()
                utils.refresh()

    def config_format_error(self):
        correct_format = {
            'answer': 'str',
            'question': 'str',
            'article': 'str',
            'options': 'str',
            'data': 'str',
            'sentences': 'str',
            'number': 'str'
            }
        correct_format = json.dumps(correct_format, indent=4)
        QMessageBox.critical(self, 'Format Error', 
        f'''<pre>Correct Format:<pre style="color:rgba(255, 0, 0, 0.8)">{correct_format}</pre></pre>
        ''', QMessageBox.StandardButton.Ok)

    def data_format_error(self, is_data=False):
        correct_format = {
                    Tools.Data: [{Tools.Answer: "str/int", Tools.Options: ["str", "..."], Tools.Question: "str", Tools.Article: "str"}]
                }
        if is_data:
            correct_format = json.dumps(correct_format[Tools.Data][0], indent=4)
        else:
            correct_format = json.dumps(correct_format, indent=4)
        QMessageBox.critical(self, 'Format Error', 
        f'''<pre>Correct Format:<pre style="color:rgba(255, 0, 0, 0.8)">{correct_format}</pre></pre>
        ''', QMessageBox.StandardButton.Ok)

def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.setWindowTitle('Sentence Label')
    main_window.show()
    return app.exec_()

if __name__ == '__main__':
    sys.exit(main())  