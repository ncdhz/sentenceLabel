from PyQt5.QtGui import QColor, QFont
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListWidget, QListWidgetItem, QTextBrowser
from utils import Tools
import utils
class ScrollPanel(QWidget):
    
    Left = 0
    
    Top = 1

    Bottom = 2

    def __init__(self, parent, panel):
        self.pt = parent
        self.panel = panel
        super(ScrollPanel, self).__init__()
        self.h_layout = QHBoxLayout(self)
        if self.panel == ScrollPanel.Left:
            self.list_widget = QListWidget(self)
        elif self.panel != ScrollPanel.Left:
            self.text_browser = QTextBrowser(self)
        
        self.font_ = QFont()
                    
        self.init_layout()
    
    def init_layout(self):
        
        if self.panel == ScrollPanel.Left:
            self.font_.setFamily('STKaiti')
            self.font_.setPixelSize(22)
            self.h_layout.addWidget(self.list_widget)
            self.list_widget.setWordWrap(True)
            self.list_widget.clicked.connect(lambda: self.list_click(self.list_widget))
            self.list_widget.setStyleSheet('''
                QListWidget::item{
                    padding:5px 0px;
                    font-size: 24px;
                }
            ''')
        elif self.panel != ScrollPanel.Left:
            self.h_layout.addWidget(self.text_browser)

        self.setLayout(self.h_layout)

    def list_click(self, lw):
        item = lw.currentItem()
        d = item.text()
        if self.pt.item_is_save(d):
            item.setForeground(QColor('black'))
        else:
            item.setForeground(QColor('red'))
        
    def refresh(self):
        if self.panel == ScrollPanel.Left:
            self.list_widget.clear()
        else:
            self.text_browser.clear()

        edit_data = self.pt.edit_data
        start = self.pt.start
        end = self.pt.end
        middle = self.pt.middle

        if middle >= start and middle < end and edit_data:
            d = edit_data[Tools.Data][middle]
            if self.panel == ScrollPanel.Left:
                los = {Tools.Article : d[Tools.Article]}
                exec(self.pt.segmentation, {}, los)
                sent_list_ = los[Tools.SentList]
                ss =  self.pt.edit_data[Tools.Data][self.pt.middle].get(Tools.Sentences, [])
                for s in sent_list_:
                    item = QListWidgetItem()
                    item.setText(s)
                    if s in ss:
                        item.setForeground(QColor('red'))
                    item.setFont(self.font_)
                    self.list_widget.addItem(item)

            elif self.panel == ScrollPanel.Top:
                ars = d[Tools.Article].split('\n')
                ar = ''.join([f'''<p style="text-indent: 30px;font-family:STKaiti;">{ar}</p>''' for ar in ars])
                self.text_browser.setText(f'''
                <div style="font-size: 22px;margin:25px;line-height: 28px;">{ar}</div>
                ''')
            else:
                a = d[Tools.Answer]
                if utils.is_int(a):
                    ai = int(a)
                else:
                    ai = ord(a.lower()) - ord('a')
                ops = ''.join([f'<p style="font-family:STKaiti;"><span style="text-decoration:underline;color:red;">{str(i + 1)}. {o}</span></p>' if i == ai else f'<p style="font-family:STKaiti;">{str(i + 1)}. {o}</p>' for i, o in enumerate(d[Tools.Options]) ])
                ls = f'''<div style="font-size: 22px;margin:25px;line-height: 28px;"><div style="font-size: 24px;font-family:STKaiti;">{d[Tools.Question]}</div>{ops}</div>'''
                self.text_browser.setText(ls)
