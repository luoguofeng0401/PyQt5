#!/usr/bin/env python
# coding: utf-8

# In[2]:


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from untitled import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

if __name__=="__main":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())


# In[ ]:




