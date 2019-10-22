# Structure of Qt5 GUI

#Imports
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow , QAction , QGridLayout, QWidget
from PyQt5.Qt import QLabel, QPushButton
from PyQt5.QtGui  import QIcon

class GUI (QMainWindow):                        
    def _init_(self):                                 
        super()._init_()                                 #initialize super class , which creates the window
        self.initUI()                                      
#__________________________________________________________________   
    def initUI(self):
        self.win.setWindowTitle('PyQt5 GUI')   #add widgets and change properties
        self.resize(400,300)
        self.add_menus_and_status()
        
        self.layout_using_grid()
#__________________________________________________________________    
    def layout_using_grid(self):
        label_1 = QLabel1('Our first label', self)                                                 #Label w/out text, window is the paren
        label_2 = QLabel2('Another label', self)
        label_span = QLabel('Label spanning columns span span span span ')
        
        button_1 = QPushButton('clik 1', self)
        button_2 = QPushButton('clik 2', self)

        grid_layout = QGridLayout()

        grid.layout.addWidget(label_1, 0, 0)                                          #row = 0 col=0
        grid.layout.addWidget(button_1, 0, 1)                                       #row = 0 col=
        grid.layout.addWidget(label_2, 1, 0)                                        #row = 1 col=0
        grid.layout.addWidget(button_2, 1, 1)                                     #row = 1 col=1

        grid_layout.addWidget(label_span, 2, 0, 1, 3)                        #row=2 col=0 rowspan=1 colspan=3
                
        grid.layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)                              #Align grid to the bottom
        grid.layout.setAlignment(label_1, Qt.AlignRight)
        grid.layout.setAlignment(label_2, Qt.AlignRight) 

        layout_widget = QWidget()                                             #create QWidget object
        layout_widget.setLayout(grid_layout)                                  #set layout

        self.setCentralWidget(layout_widget)                          #Make QWidget the central widget
#_____________________________________________________________________     
    def add_menus_and_status(self):
        self.statusBar().showMessage( 'Text in statusbar' )

        menubar = self.menuBar()                                         #create menu bar
        
        file_menu = menubar.addMenu( 'File' )                         #add menu to menu bar
        new_icon = QIcon( 'icons/new_icon.png' )                   #create icon
        new_action = QAction( new_icon, 'New',  self)             #Create an Action
        file_menu.addAction(new_action)                               #add Action to menu
        new_action.setStatusTip( 'New File' )                          #statusBar updated

        file_menu.addSeparator()                                         #add separator line between menu items

        exit_icon = QIcon( 'icons/exit_icon.png' )
        exit_action = QAction(exit_icon, 'Exit', self)
        exit_action.setStatusTip( 'Click to exit the application' )
        exit_action.triggered.connect(self.close)
        exit_action.setShortcut( 'Ctrl + Q' )
        file_menu.addAction(exit_action)
#____________________________________________________________
        edit_menu = menubar.addMenu( 'Edit' )        #add a second menu
               
if __name__ == '__main__' :
    
    app = QApplication(sys.argv)        #create application
    gui = GUI()                                  # create instance of class
    gui.show()                                   # show the constructed PyQt window
    sys.exit(app.exec_())                    # execute the application 
