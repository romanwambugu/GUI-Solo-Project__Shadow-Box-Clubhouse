import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel
from PySide6.QtGui import QPixmap, QFont
import random


class ShadowBox(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Shadow Box Clubhouse")

        self.incremnentalCounter = 0

        # Create Layout
        main_layout = QGridLayout()
        self.setLayout(main_layout)
        self.setStyleSheet("background-color: white;")

        # Add Label with Text to Layout
        font = QFont()
        font.setPointSize(50)
        font.setBold(True)

        self.message_label = QLabel("Make a Move!")
        self.message_label.setFont(font)
        main_layout.addWidget(self.message_label, 0, 2)

        self.movementText_label = QLabel("")
        self.movementText_label.setFont(font)
        main_layout.addWidget(self.movementText_label, 0, 0)

        #Add Mickey Mouse to Layout
        MickeyHead_Image = QPixmap("Image Folder/Mickey_Head.png")
        MickeyHead_Label = QLabel(self)
        MickeyHead_Label.setPixmap(MickeyHead_Image)
        main_layout.addWidget(MickeyHead_Label, 0, 1)

        #Creating Direction Buttons
        self.Up_button = QPushButton("Up")
        self.Left_button = QPushButton("Left")
        self.Right_button = QPushButton("Right")
        self.Down_button = QPushButton("Down")

        #Set Button Style - (Color/Font)
        button_style = "background-color: red; color: white; font-weight: bold;"
        button_style += f" font-size: {20}px;"
        self.Up_button.setStyleSheet(button_style)
        self.Left_button.setStyleSheet(button_style)
        self.Right_button.setStyleSheet(button_style)
        self.Down_button.setStyleSheet(button_style)

        #Set Button Height Size
        self.Up_button.setFixedHeight(60)
        self.Left_button.setFixedHeight(60)
        self.Right_button.setFixedHeight(60)
        self.Down_button.setFixedHeight(60)

        #Add Buttons to Layout
        main_layout.addWidget(self.Up_button, 1, 1)
        main_layout.addWidget(self.Left_button, 2, 0)
        main_layout.addWidget(self.Right_button, 2, 2)
        main_layout.addWidget(self.Down_button, 3, 1)

        #Connect Buttons to Functions
        self.Up_button.clicked.connect(self.User_UpButton)
        self.Left_button.clicked.connect(self.User_LeftButton)
        self.Right_button.clicked.connect(self.User_RightButton)
        self.Down_button.clicked.connect(self.User_DownButton)

    #Computer Button Functions
    def Computer_UpButton(self):
        print("Mickey Swiped Up!")
        Glove_UpImage = QPixmap("Image Folder/MickeyGlove_Up.png")
        Glove_UpLabel = QLabel(self)
        Glove_UpLabel.setPixmap(Glove_UpImage)
        self.layout().addWidget(Glove_UpLabel, 0, 1)

    def Computer_LeftButton(self):
        print("Mickey Swiped Left!")
        Glove_LeftImage = QPixmap("Image Folder/MickeyGlove_Left.png")
        Glove_LeftLabel = QLabel(self)
        Glove_LeftLabel.setPixmap(Glove_LeftImage)
        self.layout().addWidget(Glove_LeftLabel, 0, 1)

    def Computer_RightButton(self):
        print("Mickey Swiped Right!")
        Glove_RightImage = QPixmap("Image Folder/MickeyGlove_Right.png")
        Glove_RightLabel = QLabel(self)
        Glove_RightLabel.setPixmap(Glove_RightImage)
        self.layout().addWidget(Glove_RightLabel, 0, 1)

    def Computer_DownButton(self):
        print("Mickey Swiped Down!")
        Glove_DownImage = QPixmap("Image Folder/MickeyGlove_Down.png")
        Glove_DownLabel = QLabel(self)
        Glove_DownLabel.setPixmap(Glove_DownImage)
        self.layout().addWidget(Glove_DownLabel, 0, 1)

    #User Button Functions
    def User_UpButton(self):
        print("\nYou Moved Up!")
        user_choice = "Up"
        computer_choice = self.Computer_Movement()
        self.Check_Movement(user_choice, computer_choice)

    def User_LeftButton(self):
        print("\nYou Moved Left!")
        user_choice = "Left"
        computer_choice = self.Computer_Movement()
        self.Check_Movement(user_choice, computer_choice)

    def User_RightButton(self):
        print("\nYou Moved Right!")
        user_choice = "Right"
        computer_choice = self.Computer_Movement()
        self.Check_Movement(user_choice, computer_choice)

    def User_DownButton(self):
        print("\nYou Moved Down!")
        user_choice = "Down"
        computer_choice = self.Computer_Movement()
        self.Check_Movement(user_choice, computer_choice)

    #Simulate a Computer button click
    def Computer_Movement(self):
        button_list = [self.Computer_UpButton, self.Computer_LeftButton, self.Computer_RightButton, self.Computer_DownButton]
        computer_RandomButton = random.choice(button_list)
        computer_RandomButton()

        if computer_RandomButton == self.Computer_UpButton:
            return "Up"
        elif computer_RandomButton == self.Computer_LeftButton:
            return "Left"
        elif computer_RandomButton == self.Computer_RightButton:
            return "Right"
        elif computer_RandomButton == self.Computer_DownButton:
            return "Down"
        
    #Checks if User and Computer Buttons Match
    def Check_Movement(self, user_choice, computer_choice):
        self.movementText_label.setText("\nYou Moved " + user_choice + "\nMickey Moved " + computer_choice)
        if user_choice == computer_choice:
            print("You Matched!")
            self.Up_button.clicked.disconnect(self.User_UpButton)
            self.Left_button.clicked.disconnect(self.User_LeftButton)
            self.Right_button.clicked.disconnect(self.User_RightButton)
            self.Down_button.clicked.disconnect(self.User_DownButton)

            YouLose_Image = QPixmap("Image Folder/YouLose_Image.png")
            YouLose_Label = QLabel(self)
            YouLose_Label.setPixmap(YouLose_Image)
            self.layout().addWidget(YouLose_Label, 0, 1)

            self.message_label.setText("Gotcha! \nYou Lasted " + str(self.incremnentalCounter) + " Rounds!")
        else:
            print("You Didn't Match!")
            self.incremnentalCounter += 1
            self.message_label.setText(str(self.incremnentalCounter))

def main():
    app = QApplication(sys.argv)
    game = ShadowBox()
    game.show()
    game.showMaximized() # Set widget to windowed fullscreen
    app.exec()

main()