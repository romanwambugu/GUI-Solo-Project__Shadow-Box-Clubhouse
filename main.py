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
        MickeyGlove_RightImage = QPixmap("Image Folder/MickeyGlove_Right.png")
        MickeyGlove_RightLabel = QLabel(self)
        MickeyGlove_RightLabel.setPixmap(MickeyGlove_RightImage)
        main_layout.addWidget(MickeyGlove_RightLabel, 3, 0)


        MickeyGlove_UpImage = QPixmap("Image Folder/MickeyGlove_Up.png")
        MickeyGlove_UpLabel = QLabel(self)
        MickeyGlove_UpLabel.setPixmap(MickeyGlove_RightImage)
        main_layout.addWidget(MickeyGlove_UpImage, 3, 1)


        MickeyGlove_DownImage = QPixmap("Image Folder/MickeyGlove_Down.png")
        MickeyGlove_DownLabel = QLabel(self)
        MickeyGlove_DownLabel.setPixmap(MickeyGlove_RightImage)
        main_layout.addWidget(MickeyGlove_DownImage, 3, 2)


        MickeyGlove_LeftImage = QPixmap("Image Folder/MickeyGlove_Left.png")
        MickeyGlove_LeftLabel = QLabel(self)
        MickeyGlove_LeftLabel.setPixmap(MickeyGlove_RightImage)
        main_layout.addWidget(MickeyGlove_LeftImage, 3, 3)


        # Direction Buttons
        Up_button = QPushButton("Up")
        Down_button = QPushButton("Down")
        Left_button = QPushButton("Left")
        Right_button = QPushButton("Right")

        # Add Buttons to Layout
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