#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""ToolWindow.py

Copy/rename this module as a base for additional project windows,
that most conveniently use toolbars rather than menu bars,
For example:
    database lists
    data input/update forms
    forms for filtering lists

Adapted by:   twallace51@gmail.com  Cochabamba,  Bolivia
    using Linux Lubuntu, Python 3.8.2, PySide2 5.14.2,  geany 1.35   pylint3
"""
#p ylint: disable = fixme

#pylint: disable = ungrouped-imports, import-error, unused-imports

if __name__ == '__main__':
    import _RUN_ME
"""Above ensures that app starts correctly,  even if try to run this module directly"""

if 'imports':

    import sys
    import _support as glb
    from _support import(
        debug,
        sql_msg,
        pending,
        notify_,
        confirm_,
        )

    if "PySide2":
        import PySide2.QtGui            as G
        import PySide2.QtCore           as C
        import PySide2.QtWidgets        as W
        import PySide2.QtPrintSupport   as P
        import PySide2.QtSql            as S
        from   PySide2.QtCore           import Qt

class ToolWindow(W.QWidget):
    """
    """
    #TODO rename module and adapt as form, list, filter, print window
    #TODO add lines to import and create instance of class in MenuWindoe module
    #TODO update description above for usage

    def __init__(self):
        """ """
        W.QWidget.__init__(self)
        #TODO enable following and update eventFilter below,   if plan to use
        #qApp.installEventFilter(self)   #pylint: disable = undefined-variable

        if "window attributes":
            #TODO update attributes
            self.setWindowTitle("Tool bar Window")
            self.setGeometry(glb.win_placement)
            self.setMinimumSize(160, 160)

        if "QActions":
            #TODO add new/adapt following QActions
            if "to previous window":
                self.to_previous_win_act = W.QAction('Return to previous', self)
                self.to_previous_win_act.setShortcut('Ctrl+R')
                self.to_previous_win_act.setIcon(G.QIcon(glb.icons + '/actions/go-previous.png'))
                self.to_previous_win_act.triggered.connect(self.to_previous_win_handler)

            if "about app":
                self.about_app_act = W.QAction("Show List About box", self)
                self.about_app_act.setShortcut('Ctrl+A')
                self.about_app_act.setIcon(G.QIcon(glb.icons + '/actions/help-about.png'))
                self.about_app_act.triggered.connect(
                    lambda: W.QMessageBox.about(self, "About Window class module", __doc__))

            if "tool 1":
                self.tool_1_act = W.QAction("tool_1", self)
                self.tool_1_act.setIcon(G.QIcon(glb.icons + '/categories/applications-development.png'))
                self.tool_1_act.triggered.connect(pending)

            if "tool 2":
                self.tool_2_act = W.QAction("tool_2", self)
                self.tool_2_act.setIcon(G.QIcon(glb.icons + '/categories/applications-development.png'))
                self.tool_2_act.triggered.connect(pending)

            if "tool 3":
                self.tool_3_act = W.QAction("tool_3", self)
                self.tool_3_act.setIcon(G.QIcon(glb.icons + '/categories/applications-development.png'))
                self.tool_3_act.triggered.connect(pending)

            if "initial toolbar setup":
                self.tool_bar = W.QToolBar(self)
                self.tool_bar.addAction(self.to_previous_win_act)
                self.tool_bar.addAction(self.about_app_act)

                self.tool_bar.addAction(self.tool_1_act)
                self.tool_bar.addAction(self.tool_2_act)
                self.tool_bar.addAction(self.tool_3_act)

                self.tool_bar.setLayoutDirection(Qt.RightToLeft)

            if "add tool_bar to window layout":
                self.window_layout = W.QGridLayout(self)
                self.setLayout(self.window_layout)
                self.window_layout.addWidget(self.tool_bar, 0, 0, 1, 2)  # row, col, rowspan,  colspan
                self.window_layout.setRowStretch(20, 100) # push  preceding rows upward

        if "widgets":
            #TODO get db pragma for database table(s)
            #TODO create widgets for one of following

            if "table lists":
                ...
            if "input/filter forms":
                ...
            if "print reports":
                ...

        if "add widgets to window layout":
            #self.window_layout.addWidget(self.widget, 1, 0)
            ...

    if "handlers":
        def to_previous_win_handler(self):
            """by default,  back to menu_win """
            #TODO  update for actual previous window(s)
            glb.menu_win.show()
            self.hide()

    if "sub classed methods":
        #pylint: disable = invalid-name, unused-argument

        def eventFilter(self, obj, event):
            ...
            return False


        def closeEvent(self, event):
            """
            QWidget function closeEvent() run when window [X] clicked,
            is subclassed here to prevent default closing of window and app
            """
            glb.menu_win.show()
            self.hide()
