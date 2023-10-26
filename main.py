import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel
from PySide6.QtGui import QPixmap, QFont


class ShadowBox(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Shadow Box Mickey Mouse")

        # Create Layout
        main_layout = QGridLayout()
        self.setLayout(main_layout)
        self.setStyleSheet("background-color: white;")

        # Add Label with Text to Layout
        font = QFont()
        font.setPointSize(50)
        font.setBold(True)

        start_label = QLabel("Get Ready!")
        start_label.setFont(font)
        main_layout.addWidget(start_label, 0, 2)

        #Add Mickey Mouse to Layout
        MickeyHead_Image = QPixmap("Image Folder/Mickey_Head.png")
        MickeyHead_Label = QLabel(self)
        MickeyHead_Label.setPixmap(MickeyHead_Image)
        main_layout.addWidget(MickeyHead_Label, 0, 1)

        #Creating Direction Buttons
        Up_button = QPushButton("Up")
        Left_button = QPushButton("Left")
        Right_button = QPushButton("Right")
        Down_button = QPushButton("Down")

        #Set Button Style - (Color/Font)
        button_style = "background-color: red; color: white; font-weight: bold;"
        button_style += f" font-size: {20}px;"
        Up_button.setStyleSheet(button_style)
        Left_button.setStyleSheet(button_style)
        Right_button.setStyleSheet(button_style)
        Down_button.setStyleSheet(button_style)

        #Set Button Height Size
        Up_button.setFixedHeight(60)
        Left_button.setFixedHeight(60)
        Right_button.setFixedHeight(60)
        Down_button.setFixedHeight(60)

        #Add Buttons to Layout
        main_layout.addWidget(Up_button, 1, 1)
        main_layout.addWidget(Left_button, 2, 0)
        main_layout.addWidget(Right_button, 2, 2)
        main_layout.addWidget(Down_button, 3, 1)

        #Connect Buttons to Functions
        Up_button.clicked.connect(self.up_button_clicked)
        Left_button.clicked.connect(self.left_button_clicked)
        Right_button.clicked.connect(self.right_button_clicked)
        Down_button.clicked.connect(self.down_button_clicked)
        

    #Button Functions
    def up_button_clicked(self):
        print("You Moved Up!")
        Glove_UpImage = QPixmap("Image Folder/MickeyGlove_Up.png")
        Glove_UpLabel = QLabel(self)
        Glove_UpLabel.setPixmap(Glove_UpImage)
        self.layout().addWidget(Glove_UpLabel, 0, 1)

    def left_button_clicked(self):
        print("You Moved Left!")
        Glove_LeftImage = QPixmap("Image Folder/MickeyGlove_Left.png")
        Glove_LeftLabel = QLabel(self)
        Glove_LeftLabel.setPixmap(Glove_LeftImage)
        self.layout().addWidget(Glove_LeftLabel, 0, 1)

    def right_button_clicked(self):
        print("You Moved Right!")
        Glove_RightImage = QPixmap("Image Folder/MickeyGlove_Right.png")
        Glove_RightLabel = QLabel(self)
        Glove_RightLabel.setPixmap(Glove_RightImage)
        self.layout().addWidget(Glove_RightLabel, 0, 1)

    def down_button_clicked(self):
        print("You Moved Down!")
        Glove_DownImage = QPixmap("Image Folder/MickeyGlove_Down.png")
        Glove_DownLabel = QLabel(self)
        Glove_DownLabel.setPixmap(Glove_DownImage)
        self.layout().addWidget(Glove_DownLabel, 0, 1)


def main():
    app = QApplication(sys.argv)
    game = ShadowBox()
    game.show()
    game.showMaximized() # Set widget to windowed fullscreen
    app.exec_()

main()