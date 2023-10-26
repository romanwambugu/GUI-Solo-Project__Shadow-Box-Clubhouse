import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QHBoxLayout, QVBoxLayout, QLabel
from PySide6.QtGui import QPixmap


class ShadowBox(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Blank")

        # Create Layout
        main_layout = QGridLayout()
        self.setLayout(main_layout)

        # Add Images to Layout
        Glove_RightImage = QPixmap("Image Folder/MickeyGlove_Right.png")
        Glove_RightLabel = QLabel(self)
        Glove_RightLabel.setPixmap(Glove_RightImage)
        main_layout.addWidget(Glove_RightLabel, 3, 0)


        Glove_UpImage = QPixmap("Image Folder/MickeyGlove_Up.png")
        Glove_UpLabel = QLabel(self)
        Glove_UpLabel.setPixmap(Glove_UpImage)
        main_layout.addWidget(Glove_UpLabel, 3, 1)


        Glove_DownImage = QPixmap("Image Folder/MickeyGlove_Down.png")
        Glove_DownLabel = QLabel(self)
        Glove_DownLabel.setPixmap(Glove_DownImage)
        main_layout.addWidget(Glove_DownLabel, 3, 2)


        Glove_LeftImage = QPixmap("Image Folder/MickeyGlove_Left.png")
        Glove_LeftLabel = QLabel(self)
        Glove_LeftLabel.setPixmap(Glove_LeftImage)
        main_layout.addWidget(Glove_LeftLabel, 3, 3)


        #Direction Buttons
        Up_button = QPushButton("Up")
        Down_button = QPushButton("Down")
        Left_button = QPushButton("Left")
        Right_button = QPushButton("Right")

        #Add Buttons to Layout
        main_layout.addWidget(Up_button, 0, 1)
        main_layout.addWidget(Left_button, 1, 0)
        main_layout.addWidget(Right_button, 1, 2)
        main_layout.addWidget(Down_button, 2, 1)


        

def main():
    app = QApplication(sys.argv)
    game = ShadowBox()
    game.show()
    game.resize(1920, 1080)
    app.exec_()

main()