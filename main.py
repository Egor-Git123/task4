import io
import sqlite3
import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5.QtWidgets import QMainWindow, QLabel

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QTableWidget" name="tableWidget">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>20</y>
      <width>511</width>
      <height>451</height>
     </rect>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>550</x>
      <y>20</y>
      <width>241</width>
      <height>91</height>
     </rect>
    </property>
    <property name="text">
     <string>Загрузить данные</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_2">
    <property name="geometry">
     <rect>
      <x>560</x>
      <y>320</y>
      <width>231</width>
      <height>81</height>
     </rect>
    </property>
    <property name="text">
     <string>Редактировать данные</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>800</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""

tmp = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>788</width>
    <height>364</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>50</x>
      <y>50</y>
      <width>201</width>
      <height>51</height>
     </rect>
    </property>
    <property name="text">
     <string>Добавить в БД</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>560</x>
      <y>60</y>
      <width>181</width>
      <height>41</height>
     </rect>
    </property>
    <property name="text">
     <string>Изменить данные</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="lineEdit">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>130</y>
      <width>351</width>
      <height>41</height>
     </rect>
    </property>
   </widget>
   <widget class="QLabel" name="label_3">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>90</y>
      <width>351</width>
      <height>20</height>
     </rect>
    </property>
    <property name="text">
     <string>Введите: название;ст.прожарки;вид;вкус;цена;объем</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>170</y>
      <width>351</width>
      <height>28</height>
     </rect>
    </property>
    <property name="text">
     <string>Добавить</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_4">
    <property name="geometry">
     <rect>
      <x>140</x>
      <y>110</y>
      <width>81</width>
      <height>20</height>
     </rect>
    </property>
    <property name="text">
     <string>Все через ;</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_5">
    <property name="geometry">
     <rect>
      <x>390</x>
      <y>90</y>
      <width>351</width>
      <height>20</height>
     </rect>
    </property>
    <property name="text">
     <string>Введите: название;ст.прожарки;вид;вкус;цена;объем</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_6">
    <property name="geometry">
     <rect>
      <x>550</x>
      <y>110</y>
      <width>81</width>
      <height>20</height>
     </rect>
    </property>
    <property name="text">
     <string>Все через ;</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_7">
    <property name="geometry">
     <rect>
      <x>390</x>
      <y>170</y>
      <width>351</width>
      <height>20</height>
     </rect>
    </property>
    <property name="text">
     <string>Введите новые: название;ст.прожарки;вид;вкус;цена;объем</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="lineEdit_2">
    <property name="geometry">
     <rect>
      <x>370</x>
      <y>130</y>
      <width>411</width>
      <height>41</height>
     </rect>
    </property>
   </widget>
   <widget class="QLineEdit" name="lineEdit_3">
    <property name="geometry">
     <rect>
      <x>370</x>
      <y>220</y>
      <width>411</width>
      <height>41</height>
     </rect>
    </property>
   </widget>
   <widget class="QLabel" name="label_8">
    <property name="geometry">
     <rect>
      <x>560</x>
      <y>190</y>
      <width>81</width>
      <height>20</height>
     </rect>
    </property>
    <property name="text">
     <string>Все через ;</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_2">
    <property name="geometry">
     <rect>
      <x>370</x>
      <y>260</y>
      <width>411</width>
      <height>28</height>
     </rect>
    </property>
    <property name="text">
     <string>Обновить</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>788</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.pushButton.clicked.connect(self.run)
        self.pushButton_2.clicked.connect(self.open_second_form)

    def run(self):
        self.connection = sqlite3.connect("coffee.sqlite")
        self.text = "SELECT title, degree, roasting, taste, price, volume FROM types"

        res = self.connection.cursor().execute(self.text).fetchall()
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(["title", "degree", "roasting", "taste", "price", "volume"])
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))

    def open_second_form(self):
        self.second_form = SecondForm(self)
        self.second_form.show()


class SecondForm(QMainWindow):
    def __init__(self, *args):
        super().__init__()
        f = io.StringIO(tmp)
        uic.loadUi(f, self)
        self.pushButton.clicked.connect(self.add)
        self.pushButton_2.clicked.connect(self.invite)

    def add(self):
        text = self.lineEdit.text()
        text = text.split(";")
        if len(text) == 6:
            con = sqlite3.connect("coffee.sqlite")
            cur = con.cursor()
            qery1 = cur.execute(
                """Insert into types (title, degree, roasting, taste, price, volume) values (?, ?, ?, ?, ?, ?)""",
                (text[0], text[1], text[2], text[3], int(text[4]), int(text[5])))
            con.commit()

    def invite(self):
        text = self.lineEdit_2.text()
        text = text.split(";")
        text2 = self.lineEdit_3.text()
        text2 = text2.split(";")
        if len(text) == 6 and len(text2) == 6:
            con = sqlite3.connect("coffee.sqlite")
            cur = con.cursor()
            res = cur.execute("""SELECT title, degree, roasting, taste, price, volume FROM types where title = ?""",
                              (text[0],)).fetchall()
            if len(res) > 0:
                print(text2)
                res2 = cur.execute("""UPDATE types Set title = ? where title = ?""", (text2[0], text[0]))
                res3 = cur.execute("""UPDATE types Set degree = ? where title = ?""", (text2[1], text2[0]))
                res4 = cur.execute("""UPDATE types Set roasting = ? where title = ?""", (text2[2], text2[0]))
                res5 = cur.execute("""UPDATE types Set taste = ? where title = ?""", (text2[3], text2[0]))
                res6 = cur.execute("""UPDATE types Set price = ? where title = ?""", (int(text2[4]), text2[0]))
                res7 = cur.execute("""UPDATE types Set volume = ? where title = ?""", (int(text2[5]), text2[0]))
                con.commit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
