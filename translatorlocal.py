from PyQt5.QtCore import *
from PyQt5.QtWidgets import (
    QApplication, 
    QWidget, 
    QVBoxLayout,
    QHBoxLayout,
    QLabel, 
    QTextEdit,
    QScrollBar, 
    QListWidget,
    QPushButton,
    QLineEdit
)
from PyQt5.QtGui import QIcon
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)



class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("UZ - Eng translator")
        self.setWindowIcon(QIcon("communication.png"))
        self.setFixedSize(500, 600)
        self.setStyleSheet("background-color: #303030;")

        self.v_box = QVBoxLayout()
        self.h_box = QHBoxLayout()
        self.label = QLabel()

        # button qo'shish

        self.btn_convert1 = QPushButton(self)
        self.btn_convert2 = QPushButton(self)
        self.btn_convert3 = QPushButton(self)
        self.btn_convert4 = QPushButton(self)

        self.btn_convert1.setText("Add new word")
        self.btn_convert2.setText("List of words")
        self.btn_convert3.setText("Search words")
        self.btn_convert4.setText("Exit")

        self.btn_convert1.setFixedSize(300, 60)
        self.btn_convert2.setFixedSize(300, 60)
        self.btn_convert3.setFixedSize(300, 60)
        self.btn_convert4.setFixedSize(300, 60)

        self.btn_convert1.move(100, 185)
        self.btn_convert2.move(100, 265)
        self.btn_convert3.move(100, 345)
        self.btn_convert4.move(100, 425)

        self.btn_convert1.setStyleSheet("""
            QPushButton {
                border: 2px solid BLACK;
                background-color: lime;
                color: BLACK;
                border-radius: 5px;
                font-weight: bold;
                font-size: 30px; 
            }
            QPushButton:hover {
                background-color: #006400;
            }
            """)
        self.btn_convert2.setStyleSheet("""
            QPushButton {
                border: 2px solid BLACK;
                background-color: lime;
                color: BLACK;
                border-radius: 5px;
                font-weight: bold;
                font-size: 30px; 
            }
            QPushButton:hover {
                background-color: #006400;
            }
            """)
        self.btn_convert3.setStyleSheet("""
            QPushButton {
                border: 2px solid BLACK;
                background-color: lime;
                color: BLACK;
                border-radius: 5px;
                font-weight: bold;
                font-size: 30px; 
            }
            QPushButton:hover {
                background-color: #006400;
            }
            """)
        self.btn_convert4.setStyleSheet("""
            QPushButton {
                border: 2px solid BLACK;
                background-color: white;
                color: BLACK;
                border-radius: 5px;
                font-weight: bold;
                font-size: 30px; 
            }
            QPushButton:hover {
                background-color: #FF0000;
            }
            """)

        self.label_6 = QLabel("MENU", self)
        self.label_6.move(180, 90)
        self.label_6.resize(150, 60)
        self.label_6.setStyleSheet("font-size: 50px; color: #FFFF00;font-weight: bold;")

        self.btn_convert1.clicked.connect(self.add_new_word)
        self.btn_convert2.clicked.connect(self.go_to_list)
        self.btn_convert3.clicked.connect(self.go_to_search)
        self.btn_convert4.clicked.connect(self.exit)

        self.show()

    def add_new_word(self):
        self.close()
        self.btn_menu = SecondWindow()

    def go_to_list(self):
        self.close()
        self.btn_list = ThirdWindow()

    def go_to_search(self):
        self.close()
        self.btn_search = FourthWindow()

    def exit(self):
        self.close()

    

class SecondWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(500, 600)
        self.setWindowTitle("Add new word")
        self.setStyleSheet("background-color: #303030;")
        self.setWindowIcon(QIcon("communication.png"))

        self.h_box = QHBoxLayout()
        self.v_box = QVBoxLayout()
        self.v_box1 = QVBoxLayout()
        self.h_box2 = QHBoxLayout()

        self.line_1 = QLineEdit(self)
        self.line_1.setPlaceholderText("English...")
        self.line_1.setStyleSheet("""
            QLineEdit {
                border: 2px solid BLACK;
                background-color: white;
                font-weight: bold;
                font-size: 20px;
                height: 40px; 
            }
            QLineEdit:hover {
                background-color: #E0E0E0;
            }
            """)
        self.line_2 = QLineEdit(self)
        self.line_2.setPlaceholderText("Uzbek...")
        self.line_2.setStyleSheet("""
            QLineEdit {
                border: 2px solid BLACK;
                background-color: white;
                font-weight: bold;
                font-size: 20px;
                height: 40px; 
            }
            QLineEdit:hover {
                background-color: #E0E0E0;
            }
            """)
        

        self.send = QPushButton("Send  📤")
        self.send.setFixedSize(145, 40)
        self.send.setStyleSheet("""
            QPushButton {
                border: 2px solid BLACK;
                background-color: #FFD700;
                font-weight: bold;
                font-size: 20px;
                height: 43px;
                margin-left: 10px; 
            }
            QPushButton:hover {
                background-color: #808000;
            }
            """)
        

        self.btn_menu = QPushButton("Menu")
        self.btn_menu.setFixedSize(145, 40)
        self.btn_list = QPushButton("List of words")
        self.btn_list.setFixedSize(145, 40)
        self.btn1_search = QPushButton("Search")
        self.btn1_search.setFixedSize(145, 40)

#style
        
        self.btn_menu.setStyleSheet("""
            border: 2px solid;
            background: #FFFFFF;
            font-size: 20px;
            border-radius: 7px;
             """)
        self.btn_list.setStyleSheet("""
            border: 2px solid;
            background: #FFFFFF;
            font-size: 20px;
            border-radius: 7px;
             """)
        self.btn1_search.setStyleSheet("""
            border: 2px solid;
            background: #FFFFFF;
            font-size: 20px;
            border-radius: 7px;
             """)

        self.v_box1.addWidget(self.line_1)
        self.v_box1.addWidget(self.line_2)

        self.h_box2.addLayout(self.v_box1)
        self.h_box2.addWidget(self.send)

        self.h_box.addWidget(self.btn_menu)
        self.h_box.addWidget(self.btn_list)
        self.h_box.addWidget(self.btn1_search)

        self.v_box.addLayout(self.h_box2)
        self.v_box.addStretch()
        self.v_box.addLayout(self.h_box)

        self.setLayout(self.v_box)
        self.words_file = open('words.txt', 'a')
    

        self.btn_menu.clicked.connect(self.go_to_menu)
        self.btn_list.clicked.connect(self.go_to_list)
        self.send.clicked.connect(self.add_to_file)
        self.btn1_search.clicked.connect(self.go_to_search)

        self.show()

    def go_to_menu(self):
        self.close()
        self.menu = MainWindow()
        self.menu.show()

    def go_to_list(self):
        self.close()
        self.list_window = ThirdWindow()
        self.list_window.show()

    def go_to_search(self):
        self.close()
        self.btn_search1 = FourthWindow()

    def add_to_file(self):
        word = self.line_1.text() + "|" + self.line_2.text() + "\n"
        self.words_file.write(word)

        self.line_1.clear()
        self.line_2.clear()
        self.words_file.close()


class ThirdWindow(QWidget):
    def __init__(self):
        super().__init__()


        self.setWindowTitle("List of words")
        self.setFixedSize(500, 600)
        self.setStyleSheet("background-color: #303030;")
        self.setWindowIcon(QIcon("communication.png"))

        self.h_box = QHBoxLayout()
        self.h_box1 = QHBoxLayout()
        self.h_box2 = QHBoxLayout()
        self.v_box = QVBoxLayout()

        self.english = QLabel("English", self)
        self.uzbek = QLabel("Uzbek", self)
        # style

        self.english.setStyleSheet("""
            color: #CC0000;
            background-color: #404040;
            font-size: 35px;
            font-weight: bold;
        """)

        self.uzbek.setStyleSheet("""
            color: #0000FF;
            background-color: #404040;
            font-size: 35px;
            font-weight: bold;
        """)

        self.englist = QListWidget(self)
        self.englist.setStyleSheet("""
            background-color: #E0E0E0;
            font-weight: bold;
            font-size: 20px;
        """)

        self.uzblist = QListWidget(self)
        self.uzblist.setStyleSheet("""
            background-color: #E0E0E0;
            font-weight: bold;
            font-size: 20px;
        """)

        # Enable scrollbars for the QListWidget widgets
        self.englist.setVerticalScrollBar(QScrollBar())
        self.uzblist.setVerticalScrollBar(QScrollBar())

        self.btn_menu = QPushButton("Menu")
        self.btn_menu.setFixedSize(145, 40)
        self.btn_add = QPushButton("Add new word")
        self.btn_add.setFixedSize(145, 40)
        self.btn_search = QPushButton("Search")
        self.btn_search.setFixedSize(145, 40)

        # style past

        self.btn_menu.setStyleSheet("""
            border: 2px solid;
            background: #FFFFFF;
            font-size: 20px;
            border-radius: 7px;
        """)
        self.btn_add.setStyleSheet("""
            border: 2px solid;
            background: #FFFFFF;
            font-size: 20px;
            border-radius: 7px;
        """)
        self.btn_search.setStyleSheet("""
            border: 2px solid;
            background: #FFFFFF;
            font-size: 20px;
            border-radius: 7px;
        """)

        self.h_box2.addWidget(self.btn_menu)
        self.h_box2.addWidget(self.btn_add)
        self.h_box2.addWidget(self.btn_search)

        self.h_box.addWidget(self.english)
        self.h_box.addWidget(self.uzbek)
        self.h_box1.addWidget(self.englist)
        self.h_box1.addWidget(self.uzblist)

        self.v_box.addLayout(self.h_box)
        self.v_box.addSpacing(20)
        self.v_box.addLayout(self.h_box1)
        self.v_box.addSpacing(20)
        self.v_box.addLayout(self.h_box2)

        self.scroll_bar1 = self.englist.verticalScrollBar()
        self.scroll_bar2 = self.uzblist.verticalScrollBar()
        self.setLayout(self.v_box)

        self.scroll_bar1.valueChanged.connect(self.scrollBarValueChanged1)
        self.scroll_bar2.valueChanged.connect(self.scrollBarValueChanged2)
        
        self.btn_menu.clicked.connect(self.go_to_menu)
        self.btn_add.clicked.connect(self.go_to_add)
        self.btn_search.clicked.connect(self.go_to_search)
        self.load_words()

        self.show()

    def go_to_menu(self):
        self.close()
        self.menu = MainWindow()
        self.menu.show()

    def go_to_add(self):
        self.close()
        self.add = SecondWindow()
        self.add.show()

    def go_to_search(self):
        self.close()
        self.btn_search = FourthWindow()

#scrollbars
        
    def scrollBarValueChanged1(self, value):
        self.scroll_bar2.setValue(value)
    def scrollBarValueChanged2(self, value):
        self.scroll_bar1.setValue(value)

    def load_words(self):
        with open("words.txt", "r") as file:
            words = [line.strip().split("|") for line in file]
            sorted_words = sorted(words, key=lambda x: x[0])

        for i, word in enumerate(sorted_words, start=1):
            self.englist.addItem(f"{i}. {word[0]}")
            self.uzblist.addItem(f"{i}. {word[1]}")

class FourthWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Search Word")
        self.setFixedSize(500, 600)
        self.setStyleSheet("background-color: #303030;")
        self.setWindowIcon(QIcon("communication.png"))


        self.input = QLineEdit()
        self.input.setPlaceholderText('Enter a word...')
        self.input.setStyleSheet("""
            background-color: #E0E0E0;
            font-weight: bold;
            font-size: 20px;                    
            height: 40px;""")


        self.btn = QPushButton(' Search 🔍')
        self.btn.setStyleSheet("""
            font-size: 20px;
            background-color: #0000FF;
            font-weight: bold;
            height: 43px; 
            margin-left: 10px;""")
        


        self.btn_cleaning = QPushButton('  Clean   🧹')
        self.btn_cleaning.setFixedSize(230, 40)
        self.btn_cleaning.setStyleSheet("""
            font-size: 25px;
            background-color: #fccb06;
            border-radius: 7px;
            font-weight: bold;
        """)


        self.change_lang = QPushButton(' 🇺🇿 UZ   🔁   ENG 🇬🇧 ')
        self.change_lang.setFixedSize(230, 40)
        self.change_lang.setStyleSheet("""
            font-size: 25px;
            background-color: #b1ddf1;
            border-radius: 7px;
            font-weight: bold;
        """)
        


        self.h_top = QHBoxLayout()
        self.h_top.addWidget(self.input)
        self.h_top.addWidget(self.btn)


        self.list = QListWidget()
        self.list.setStyleSheet("""
            color: #FFFF00;
            background-color: #404040;
            font-size: 30px;
            font-weight: bold;
        """)

        self.menu = QPushButton('Menu')
        self.menu.setFixedSize(145, 40)
        self.lsword = QPushButton('List of Words')
        self.lsword.setFixedSize(145, 40)
        self.add_word = QPushButton('Add new word')
        self.add_word.setFixedSize(145, 40)

        #style
        self.menu.setStyleSheet("""
            border: 2px solid;
            background: #FFFFFF;
            font-size: 20px;
            border-radius: 7px;
             """)
        self.lsword.setStyleSheet("""
            border: 2px solid;
            background: #FFFFFF;
            font-size: 20px;                      
            border-radius: 7px;
             """)
        self.add_word.setStyleSheet("""
            border: 2px solid;
            background: #FFFFFF;
            font-size: 20px;
            border-radius: 7px;
             """)



        self.v_main = QVBoxLayout()
        self.h_pastki = QHBoxLayout()
        self.h_box = QHBoxLayout()
#h_box
        self.h_pastki.addWidget(self.menu)
        self.h_pastki.addWidget(self.lsword)
        self.h_pastki.addWidget(self.add_word)
        self.h_box.addWidget(self.change_lang)
        self.h_box.addSpacing(10)
        self.h_box.addWidget(self.btn_cleaning)
# v box 
        self.v_main.addLayout(self.h_top)
        self.v_main.addSpacing(15)
        self.v_main.addLayout(self.h_box)
        self.v_main.addSpacing(15)
        self.v_main.addWidget(self.list)
        self.v_main.addSpacing(15)
        self.v_main.addLayout(self.h_pastki)

        self.setLayout(self.v_main)
#click
        

        self.menu.clicked.connect(self.menu_click)
        self.lsword.clicked.connect(self.lowlist0)
        self.add_word.clicked.connect(self.wordlist_click)
        self.btn.clicked.connect(self.add_search)
        self.btn_cleaning.clicked.connect(self.cleaning_click)
        self.change_lang.clicked.connect(self.lang_change)

        self.show()

#connection metods
        

    def menu_click(self):
        self.close()
        self.menu = MainWindow()

    def wordlist_click(self):
        self.close()
        self.addnewWord = SecondWindow()
    
    def lowlist0(self):
        self.close()
        self.lowlist = ThirdWindow()
    
    def lang_change(self):

        if self.change_lang.text() == ' 🇺🇿 UZ   🔁   ENG 🇬🇧 ':
            self.change_lang.setText(' 🇬🇧 ENG   🔁   UZ  🇺🇿   ')
        else:
            self.change_lang.setText(' 🇺🇿 UZ   🔁   ENG 🇬🇧 ')





    def add_search(self):
        text = self.input.text()
        if len(text) > 1:
            with open("words.txt", 'r') as file:
                dates = file.readlines()
                count = 0
                for data in dates:
                    eng, uzb = data.strip().split('|')
                    if text.lower() == eng.lower():
                        self.list.addItem(uzb)
                    elif text.lower() == uzb.lower():
                        self.list.addItem(eng)
                    else:
                        count += 1
                if count == len(dates):
                    self.list.addItem('  Word not found  🤷')


    def cleaning_click(self):
        self.input.clear()
        self.list.clear()

        
app = QApplication([])
main = MainWindow()
# second = SecondWindow()
# third = ThirdWindow()
# four = FourthWindow()
app.exec_()