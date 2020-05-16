#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""_RUN_ME.py - template for starting a new python project ...

This module is a foundation for developing PySide2 projects, by providing:
    a start script (this file ...)
    a menu window - for navigating to any other windows or actions added to project
    a sample toolbar window,  as a template for other windows

    Recomendation: dont modify the ToolWindow.py module directly,
    but copy/rename it,  for adapting into other windows,   for example:
        form windows
        table windows
        filter windows
    For demo,   see "../_SimpleDbDemo/_README.gny"

Note:  this demo also depends "_support.py! for:
    global variables
    generic utility methods

Usage:   See "_README.gny"

Adapted by:   twallace51@gmail.com
    Cochabamba,  Bolivia
    using Linux Lubuntu, Python 3.8.2, PySide2 5.14.2,  geany 1.35   pylint3
"""

#p ylint: disable = fixme

#TODO  rewrite documentation above for actual project where this module was copied to ...
#         eg goals, description, plans, etc

#pylint: disable = unused-import, import-error

if "imports":

    import sys
    import _support as glb          # for keeping global variables as glb.<variable_name>
    from _support   import(
        debug,
        sql_msg,
        notify_,
        confirm_,
        get_window_placement,
        open_database,
        unauthorized_msg,
        pending,
        )

    if "PySide2":
        import PySide2.QtGui          as G
        import PySide2.QtCore         as C
        import PySide2.QtWidgets      as W
        import PySide2.QtPrintSupport as P
        import PySide2.QtSql          as S
        from   PySide2.QtCore import Qt     # ie Qt environment constants

class MenuWindow(W.QWidget):
    """ MenuWindow class provides a basic menu bar, allowing:
            admin login
            about messages
            eventFilter
    """

    def __init__(self):
        W.QWidget.__init__(self)

        if "attributes":
            self.setWindowTitle("Main Window")
            self.setMinimumSize(200, 200)
            self.setGeometry(glb.win_placement)

        if "menu bar options":

            if "QActions":
                self.login_act = W.QAction("Enter Admin password to enable admin menus", self)
                self.login_act.setIcon(G.QIcon(glb.icons + '/apps/preferences-desktop-user-password.png'))
                self.login_act.triggered.connect(self.login_handler)

                self.about_qt_act = W.QAction("Show the Qt library's About box", self)
                self.about_qt_act.setIcon(G.QIcon(glb.icons + '/actions/help-about.png'))
                self.about_qt_act.triggered.connect(W.QApplication.instance().aboutQt)    #self.about_qt_act.triggered.connect(qApp.aboutQt) # also works

                self.about_app_act = W.QAction("Show the application's About box", self)
                self.about_app_act.setShortcut("Ctrl+A")
                self.about_app_act.setIcon(G.QIcon(glb.icons + '/actions/help-about.png'))
                self.about_app_act.triggered.connect(lambda: notify_("About MenuWindow", __doc__))

                self.option_1_act = W.QAction("Tool Window", self)
                self.option_1_act.setShortcut("Ctrl+1")
                self.option_1_act.setIcon(G.QIcon(glb.icons + '/categories/system-help.png'))
                self.option_1_act.triggered.connect(self.open_toolwindow_handler)

                self.option_2_act = W.QAction("Option message", self)
                self.option_2_act.setShortcut("Ctrl+2")
                self.option_2_act.setIcon(G.QIcon(glb.icons + '/categories/system-help.png'))
                self.option_2_act.triggered.connect(pending)

                self.option_3_act = W.QAction("Option message", self)
                self.option_3_act.setShortcut("Ctrl+3")
                self.option_3_act.setIcon(G.QIcon(glb.icons + '/categories/system-help.png'))
                self.option_3_act.triggered.connect(pending)

                self.admin_1_act = W.QAction("Admin option 1", self)
                self.admin_1_act.setIcon(G.QIcon(glb.icons + '/categories/system-help.png'))
                self.admin_1_act.triggered.connect(self.admin_option_handler)

                self.admin_2_act = W.QAction("Admin option 2", self)
                self.admin_2_act.setIcon(G.QIcon(glb.icons + '/categories/system-help.png'))
                self.admin_2_act.triggered.connect(self.admin_option_handler)

                self.admin_3_act = W.QAction("Admin option 3", self)
                self.admin_3_act.setIcon(G.QIcon(glb.icons + '/categories/system-help.png'))
                self.admin_3_act.triggered.connect(self.admin_option_handler)

        if "menu bar layout":

            self.menu_mbr = W.QMenuBar()

            if "Menu":
                self.main_mnu = self.menu_mbr.addMenu("&Menu")

                self.main_mnu.addAction(self.option_1_act)
                self.main_mnu.addAction(self.option_2_act)
                self.main_mnu.addAction(self.option_3_act)

            if "Admin":
                self.admin_mnu = self.menu_mbr.addMenu("&Admin")
                self.admin_mnu.addAction(self.login_act)

                self.admin_mnu.addAction(self.admin_1_act)
                self.admin_mnu.addAction(self.admin_2_act)
                self.admin_mnu.addAction(self.admin_3_act)

            if "About":
                self.about_mnu = self.menu_mbr.addMenu("About")
                self.about_mnu.addAction(self.about_qt_act)
                self.about_mnu.addAction(self.about_app_act)

        if "window_layout":
            self.window_layout = W.QGridLayout(self)
            self.setLayout(self.window_layout)

            self.window_layout.setMenuBar(self.menu_mbr)

    if "connection handlers":

        def admin_option_handler(self):
            """ """
            if glb.current_user not in glb.admin_users_list:
                unauthorized_msg(glb.current_user)
                return
            pending()

        def login_handler(self):
            """
            To limit access of individual options in a project, to specific users,
            require that users login with valid passwords,  based on glb.admin_list.
            If login is valid,  set glb.current_user to user_name.
            Then, at the begining of each restricted option,  check if current_user is authorized or not to continue ...
            For example,   see admin_option_handler() above
            """
            user, ok_ = W.QInputDialog().getText(
                self,
                "Enter",
                "User name:".ljust(60),
                W.QLineEdit.Normal)
            if ok_ and user:
                passwd, ok_ = W.QInputDialog().getText(
                    self,
                    "Enter",
                    "Password:".ljust(60),
                    W.QLineEdit.Normal)
                if ok_ and passwd:
                    user = user.strip()
                    passwd = passwd.strip()
                    if (user, passwd) in glb.user_list:
                        glb.current_user = user
                        msg = '<h3 style="color: green;">Login and/or password are accepted - \nlogged in as \n{}</h3>'.format(user)
                        notify_("VALID", msg)
                        return
            glb.current_user = "guest"
            msg = '<h3 style="color: red;">Login and/or password are invalid - \nlogged in as </h3>\nGuest'
            notify_("INVALID", msg)

        def open_toolwindow_handler(self):
            """ """
            self.hide()
            glb.tool_win.show()

    if "subclassed functions":

        def eventFilter(self, obj, event):  #pylint: disable = no-self-use
            """use a generic eventFilter() _support.py,
            or write a custom global one here for project"""
            glb.show_most_events(obj, event)
            return False

if "project start script":
    glb.green(__doc__)
    app = W.QApplication()

    if "initialize global variables used by project":

        glb.icons = "/usr/share/icons/oxygen/base/32x32"  # my prefered icon set

        if "customize window placement":
            glb.win_placement = get_window_placement(app)[0]
            glb.screen_size = get_window_placement(app)[1]

        if not "enable here to open project database":
            #TODO create database tables and fields
            open_database("database_name.db")

        if "set default window placement parameters":
            glb.screen_size = C.QSize(1920, 1050)                    # default screen_size
            glb.win_placement = C.QRect(800, 80, 500, 670)        # default window placement and size

    if "Admin controls":
        """Based on current user's login name,  admin priveleges can be given
        either individually or to those found in admin list
        Test for current user's name at begining of restricted options."""
        glb.current_user = "Guest"  # Guest has no admin priveleges
        glb.user_list = [
            ("tim", "123"),
            ("Admin", "admin"),
            ("Peter", "peter"),
            ("Paul", "paul"),
            ("Mary", "mary")
            ]
        glb.admin_users_list = [
            ("Admin"),
            ("tim")
            ]

        if not "enable for automatic Admin priveleges during development":
            glb.current_user = "Admin"

    if "project modules":
        if "import project modules":
            #TODO - add other project modules here
            from ToolWindow import ToolWindow

        if "create project windows":
            """make addresses to windows available to all as glb.<window> = Window()"""
            #TODO - add other project class instances here
            glb.menu_win = MenuWindow()
            glb.tool_win = ToolWindow()

    if not "enable here to run global event filter during development":
        """enable above to see in terminal ~many~ (almost all) events occuring in the application,
        including events in class instances and children widgets.
        The events pass thru the eventFilter() of an instance of MenuWindow()
        """
        qApp.installEventFilter(MenuWindow())        #pylint: disable = undefined-variable

    if "open Menu window":
        glb.menu_win.show()

    """Remember: __init__ of each of above class/modules are run last,  here ... """

    if "start app ....":
        app.exec_()
        sys.exit()
