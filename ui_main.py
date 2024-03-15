# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainYYaJtK.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################


from PySide6.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide6.QtWidgets import *

import images.resources as resources
#font.setLegacyWeight(75)
#font1.setLegacyWeight(75)
#font2.setLegacyWeight(75)
#font3.setLegacyWeight(75)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1046, 599)
        icon = QIcon()
        icon.addFile(u":/icons/planner.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolButtonStyle(Qt.ToolButtonIconOnly)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QTabWidget.Rounded)
        MainWindow.setDockNestingEnabled(True)
        MainWindow.setDockOptions(QMainWindow.AllowNestedDocks|QMainWindow.AllowTabbedDocks|QMainWindow.AnimatedDocks|QMainWindow.ForceTabbedDocks|QMainWindow.GroupedDragging|QMainWindow.VerticalTabs)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QFrame {\n"
"	\n"
"	background-color: rgb(233, 236, 239);\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 40))
        self.frame_2.setStyleSheet(u"QFrame{\n"
"background-color:#212529;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton{\n"
"	background-color: transparent;\n"
"	border-radius: 5px;\n"
"	border-style: none;\n"
"}\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(3, 3, 3, 3)
        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 0, 0, 0)
        self.pushButton_18 = QPushButton(self.frame)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setIcon(icon)
        self.pushButton_18.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.pushButton_18)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 3, 14, 3)
        self.pushButton_2 = QPushButton(self.frame_4)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon1 = QIcon()
        icon1.addFile(u":/icons/minus-sign.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.pushButton_4 = QPushButton(self.frame_4)
        self.pushButton_4.setObjectName(u"pushButton_4")
        icon2 = QIcon()
        icon2.addFile(u":/icons/resize (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon2)
        self.pushButton_4.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.pushButton_4)

        self.pushButton_3 = QPushButton(self.frame_4)
        self.pushButton_3.setObjectName(u"pushButton_3")
        icon3 = QIcon()
        icon3.addFile(u":/icons/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon3)
        self.pushButton_3.setIconSize(QSize(18, 18))

        self.horizontalLayout_2.addWidget(self.pushButton_3)


        self.horizontalLayout.addWidget(self.frame_4, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.frame_2)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1044, 485))
        self.horizontalLayout_4 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.scrollAreaWidgetContents)
        if (self.tableWidget.columnCount() < 7):
            self.tableWidget.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"QTableWidget {\n"
"    background-color: #ffffff; /* Colore di sfondo della tabella */\n"
"    border: 1px solid #CED4DA; /* Bordo della tabella */\n"
"}\n"
"\n"
"QTableWidget QHeaderView::section {\n"
"    background-color: #495057;\n"
"    color: #ffffff; /* Colore del testo degli header orizzontali */\n"
"    border: none;\n"
"    padding: 8px;\n"
"    font-weight: bold; /* Testo in grassetto */\n"
"}\n"
"\n"
"QTableWidget::verticalHeader {\n"
"    background-color: #CED4DA; /* Colore degli header verticali */\n"
"    color: #212529; /* Colore del testo degli header verticali */\n"
"    font-weight: bold; /* Testo in grassetto */\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    padding: 10px; /* Spaziatura interna delle celle */\n"
"    border-bottom: 1px solid #CED4DA; /* Bordo inferiore delle celle */\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: #E6E6E6; /* Colore di sfondo della cella selezionata */\n"
"}\n"
"\n"
"QTableWidget QHeaderView::section {\n"
"    padding: 8px;\n"
"}\n"
"\n"
""
                        "QTableWidget QHeaderView::section:horizontal {\n"
"    background-color: #ADB5BD; /* Colore per gli header orizzontali */\n"
"    color: #212529; /* Colore del testo per gli header orizzontali */\n"
"    font-weight: bold; /* Testo in grassetto */\n"
"}\n"
"\n"
"QTableWidget QHeaderView::section:vertical {\n"
"    background-color: #DEE2E6; /* Colore per gli header verticali */\n"
"    color: #212529; /* Colore del testo per gli header verticali */\n"
"    font-weight: bold; /* Testo in grassetto */\n"
"}\n"
"")
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setAutoScrollMargin(18)
        self.tableWidget.setDragEnabled(False)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setGridStyle(Qt.NoPen)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(100)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setMinimumSectionSize(50)
        self.tableWidget.verticalHeader().setDefaultSectionSize(50)
        self.tableWidget.verticalHeader().setProperty("showSortIndicator", True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_4.addWidget(self.tableWidget)

        self.frame_9 = QFrame(self.scrollAreaWidgetContents)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy1)
        self.frame_9.setAutoFillBackground(False)
        self.frame_9.setStyleSheet(u"QFrame{\n"
" \n"
"	background-color:#E9ECEF;\n"
"}\n"
"\n"
"QTextEdit{\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_9)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.frame_9)
        self.frame_12.setObjectName(u"frame_12")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy2)
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_12)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.frame_12)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setLegacyWeight(75)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(33, 37, 41);")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_2)


        self.verticalLayout_2.addWidget(self.frame_12)

        self.frame_11 = QFrame(self.frame_9)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_11)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.frame_11)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_13)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_12 = QPushButton(self.frame_13)
        self.pushButton_12.setObjectName(u"pushButton_12")
        icon4 = QIcon()
        icon4.addFile(u":/icons/list.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_12.setIcon(icon4)

        self.gridLayout.addWidget(self.pushButton_12, 1, 0, 1, 1)

        self.pushButton_13 = QPushButton(self.frame_13)
        self.pushButton_13.setObjectName(u"pushButton_13")
        icon5 = QIcon()
        icon5.addFile(u":/icons/list (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_13.setIcon(icon5)

        self.gridLayout.addWidget(self.pushButton_13, 1, 1, 1, 1)

        self.pushButton_7 = QPushButton(self.frame_13)
        self.pushButton_7.setObjectName(u"pushButton_7")
        icon6 = QIcon()
        icon6.addFile(u":/icons/bold.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(icon6)

        self.gridLayout.addWidget(self.pushButton_7, 2, 0, 1, 1)

        self.comboBox = QComboBox(self.frame_13)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        font2 = QFont()
        font2.setBold(True)
        font2.setLegacyWeight(75)
        self.comboBox.setFont(font2)
        self.comboBox.setStyleSheet(u"")
        self.comboBox.setDuplicatesEnabled(False)
        self.comboBox.setFrame(True)

        self.gridLayout.addWidget(self.comboBox, 0, 0, 1, 1)

        self.pushButton_10 = QPushButton(self.frame_13)
        self.pushButton_10.setObjectName(u"pushButton_10")
        icon7 = QIcon()
        icon7.addFile(u":/icons/italic-font.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_10.setIcon(icon7)

        self.gridLayout.addWidget(self.pushButton_10, 2, 2, 1, 1)

        self.pushButton_17 = QPushButton(self.frame_13)
        self.pushButton_17.setObjectName(u"pushButton_17")
        icon8 = QIcon()
        icon8.addFile(u":/icons/marker.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_17.setIcon(icon8)

        self.gridLayout.addWidget(self.pushButton_17, 0, 1, 1, 1)

        self.pushButton_11 = QPushButton(self.frame_13)
        self.pushButton_11.setObjectName(u"pushButton_11")
        icon9 = QIcon()
        icon9.addFile(u":/icons/underline-text.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_11.setIcon(icon9)

        self.gridLayout.addWidget(self.pushButton_11, 2, 1, 1, 1)

        self.pushButton_14 = QPushButton(self.frame_13)
        self.pushButton_14.setObjectName(u"pushButton_14")
        icon10 = QIcon()
        icon10.addFile(u":/icons/palette.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_14.setIcon(icon10)

        self.gridLayout.addWidget(self.pushButton_14, 0, 2, 1, 1)

        self.pushButton = QPushButton(self.frame_13)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 1, 2, 1, 1)


        self.verticalLayout_4.addWidget(self.frame_13)

        self.textEdit = QTextEdit(self.frame_11)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setStyleSheet(u"QTextEdit {\n"
"    background-color: #ffffff; /* Colore di sfondo bianco */\n"
"    border: 1px solid #cccccc; /* Bordo sottile grigio */\n"
"    color: #333333; /* Colore del testo nero */\n"
"    font-size: 14px; /* Dimensione del carattere */\n"
"    padding: 8px; /* Spaziatura interna */\n"
"}\n"
"")
        self.textEdit.setTabChangesFocus(False)

        self.verticalLayout_4.addWidget(self.textEdit)


        self.verticalLayout_2.addWidget(self.frame_11)

        self.frame_10 = QFrame(self.frame_9)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy2.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy2)
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.pushButton_8 = QPushButton(self.frame_10)
        self.pushButton_8.setObjectName(u"pushButton_8")
        font3 = QFont()
        font3.setBold(True)
        font3.setUnderline(False)
        font3.setLegacyWeight(75)
        font3.setStrikeOut(False)
        self.pushButton_8.setFont(font3)
        self.pushButton_8.setStyleSheet(u"QPushButton {\n"
"    background-color: #ADB5BD; /* Colore di sfondo */\n"
"    border: none; /* Nessun bordo */\n"
"    color: #ecf0f1; /* Colore del testo */\n"
"    text-align: center; /* Allineamento del testo al centro */\n"
"    text-decoration: none; /* Nessuna decorazione del testo */\n"
"    display: inline-block; /* Impostazione inline-block per adattarsi al contenuto */\n"
"    font-size: 12px; /* Dimensione del carattere */\n"
"    cursor: pointer; /* Cursore del mouse */\n"
"    border-radius: 10px; /* Bordo arrotondato */\n"
"    transition-duration: 0.4s; /* Durata dell'animazione durante il passaggio */\n"
"	padding: 8px;\n"
"	margin: 2px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #9ca3ab; /* Cambia il colore di sfondo al passaggio del mouse */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #95a2aa; /* Colore di sfondo simile al pressed */\n"
"}\n"
"")
        icon11 = QIcon()
        icon11.addFile(u":/icons/bin.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon11)

        self.horizontalLayout_8.addWidget(self.pushButton_8)

        self.pushButton_9 = QPushButton(self.frame_10)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setFont(font3)
        self.pushButton_9.setStyleSheet(u"QPushButton {\n"
"    background-color: #ADB5BD; /* Colore di sfondo */\n"
"    border: none; /* Nessun bordo */\n"
"    color: #ecf0f1; /* Colore del testo */\n"
"    text-align: center; /* Allineamento del testo al centro */\n"
"    text-decoration: none; /* Nessuna decorazione del testo */\n"
"    display: inline-block; /* Impostazione inline-block per adattarsi al contenuto */\n"
"    font-size: 12px; /* Dimensione del carattere */\n"
"    cursor: pointer; /* Cursore del mouse */\n"
"    border-radius: 10px; /* Bordo arrotondato */\n"
"    transition-duration: 0.4s; /* Durata dell'animazione durante il passaggio */\n"
"	padding: 8px;\n"
"	margin: 2px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #9ca3ab; /* Cambia il colore di sfondo al passaggio del mouse */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #95a2aa; /* Colore di sfondo simile al pressed */\n"
"}\n"
"")
        icon12 = QIcon()
        icon12.addFile(u":/icons/diskette.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_9.setIcon(icon12)

        self.horizontalLayout_8.addWidget(self.pushButton_9)


        self.verticalLayout_2.addWidget(self.frame_10)


        self.horizontalLayout_4.addWidget(self.frame_9)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.frame_5 = QFrame(self.centralwidget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"QFrame{\n"
" \n"
"	background-color:rgb(233, 236, 239);\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy3)
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 0, 0, 0)
        self.pushButton_6 = QPushButton(self.frame_6)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(150, 0))
        self.pushButton_6.setMaximumSize(QSize(80, 16777215))
        self.pushButton_6.setFont(font3)
        self.pushButton_6.setStyleSheet(u"QPushButton {\n"
"    background-color: #ADB5BD; /* Colore di sfondo */\n"
"    border: none; /* Nessun bordo */\n"
"    color: #ecf0f1; /* Colore del testo */\n"
"    text-align: center; /* Allineamento del testo al centro */\n"
"    text-decoration: none; /* Nessuna decorazione del testo */\n"
"    display: inline-block; /* Impostazione inline-block per adattarsi al contenuto */\n"
"    font-size: 12px; /* Dimensione del carattere */\n"
"    cursor: pointer; /* Cursore del mouse */\n"
"    border-radius: 10px; /* Bordo arrotondato */\n"
"    transition-duration: 0.4s; /* Durata dell'animazione durante il passaggio */\n"
"	padding: 4px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #9ca3ab; /* Cambia il colore di sfondo al passaggio del mouse */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #95a2aa; /* Colore di sfondo simile al pressed */\n"
"}\n"
"")
        icon13 = QIcon()
        icon13.addFile(u":/icons/clock2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon13)

        self.horizontalLayout_6.addWidget(self.pushButton_6)


        self.horizontalLayout_5.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_5)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pushButton_15 = QPushButton(self.frame_8)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setFont(font3)
        self.pushButton_15.setStyleSheet(u"QPushButton {\n"
"    background-color: #ADB5BD; /* Colore di sfondo */\n"
"    border: none; /* Nessun bordo */\n"
"    color: #ecf0f1; /* Colore del testo */\n"
"    text-align: center; /* Allineamento del testo al centro */\n"
"    text-decoration: none; /* Nessuna decorazione del testo */\n"
"    display: inline-block; /* Impostazione inline-block per adattarsi al contenuto */\n"
"    font-size: 12px; /* Dimensione del carattere */\n"
"    cursor: pointer; /* Cursore del mouse */\n"
"    border-radius: 10px; /* Bordo arrotondato */\n"
"    transition-duration: 0.4s; /* Durata dell'animazione durante il passaggio */\n"
"	padding: 4px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #9ca3ab; /* Cambia il colore di sfondo al passaggio del mouse */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #95a2aa; /* Colore di sfondo simile al pressed */\n"
"}\n"
"")
        icon14 = QIcon()
        icon14.addFile(u":/icons/prevoius.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_15.setIcon(icon14)

        self.horizontalLayout_7.addWidget(self.pushButton_15)

        self.pushButton_16 = QPushButton(self.frame_8)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setFont(font3)
        self.pushButton_16.setStyleSheet(u"QPushButton {\n"
"    background-color: #ADB5BD; /* Colore di sfondo */\n"
"    border: none; /* Nessun bordo */\n"
"    color: #ecf0f1; /* Colore del testo */\n"
"    text-align: center; /* Allineamento del testo al centro */\n"
"    text-decoration: none; /* Nessuna decorazione del testo */\n"
"    display: inline-block; /* Impostazione inline-block per adattarsi al contenuto */\n"
"    font-size: 12px; /* Dimensione del carattere */\n"
"    cursor: pointer; /* Cursore del mouse */\n"
"    border-radius: 10px; /* Bordo arrotondato */\n"
"    transition-duration: 0.4s; /* Durata dell'animazione durante il passaggio */\n"
"	padding: 4px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #9ca3ab; /* Cambia il colore di sfondo al passaggio del mouse */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #95a2aa; /* Colore di sfondo simile al pressed */\n"
"}\n"
"")
        icon15 = QIcon()
        icon15.addFile(u":/icons/pdf-file.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_16.setIcon(icon15)

        self.horizontalLayout_7.addWidget(self.pushButton_16)

        self.pushButton_5 = QPushButton(self.frame_8)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setFont(font3)
        self.pushButton_5.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_5.setStyleSheet(u"QPushButton {\n"
"    background-color: #ADB5BD; /* Colore di sfondo */\n"
"    border: none; /* Nessun bordo */\n"
"    color: #ecf0f1; /* Colore del testo */\n"
"    text-align: center; /* Allineamento del testo al centro */\n"
"    text-decoration: none; /* Nessuna decorazione del testo */\n"
"    display: inline-block; /* Impostazione inline-block per adattarsi al contenuto */\n"
"    font-size: 12px; /* Dimensione del carattere */\n"
"    cursor: pointer; /* Cursore del mouse */\n"
"    border-radius: 10px; /* Bordo arrotondato */\n"
"    transition-duration: 0.4s; /* Durata dell'animazione durante il passaggio */\n"
"	padding: 4px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #9ca3ab; /* Cambia il colore di sfondo al passaggio del mouse */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #95a2aa; /* Colore di sfondo simile al pressed */\n"
"}\n"
"")
        icon16 = QIcon()
        icon16.addFile(u":/icons/next-week.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon16)

        self.horizontalLayout_7.addWidget(self.pushButton_5)


        self.horizontalLayout_5.addWidget(self.frame_8)


        self.verticalLayout.addWidget(self.frame_5)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 30))
        self.frame_3.setMaximumSize(QSize(16777215, 30))
        self.frame_3.setStyleSheet(u"QFrame{\n"
"background-color:#212529;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton{\n"
"	background-color: transparent;\n"
"	border-radius: 0px;\n"
"	border-style: none;\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_3)


        self.verticalLayout.addWidget(self.frame_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Week Planner", None))
        self.pushButton_18.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"La tua settimana", None))
        self.pushButton_2.setText("")
        self.pushButton_4.setText("")
        self.pushButton_3.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Luned\u00ec", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Marted\u00ec", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Mercoled\u00ec", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Gioved\u00ec", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Venerd\u00ec", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Sabato", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Domenica", None));
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Titolo", None))
        self.pushButton_12.setText("")
        self.pushButton_13.setText("")
        self.pushButton_7.setText("")
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Paragrafo", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Titolo", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Sottotitolo", None))

        self.comboBox.setCurrentText(QCoreApplication.translate("MainWindow", u"Paragrafo", None))
        self.pushButton_10.setText("")
        self.pushButton_17.setText("")
        self.pushButton_11.setText("")
        self.pushButton_14.setText("")
        self.pushButton.setText("")
        self.textEdit.setPlaceholderText("")
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Cancella", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Salva", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Aggiungi un orario", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"Settimana precedente", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"Salva PDF", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Prossima settimana", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Week Planner - Marion \u00a9", None))
    # retranslateUi

