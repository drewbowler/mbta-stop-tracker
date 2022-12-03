# Form implementation generated from reading ui file 'mbta_tracker.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_mbta_tracker_window(object):
    def setupUi(self, mbta_tracker_window):
        mbta_tracker_window.setObjectName("mbta_tracker_window")
        mbta_tracker_window.resize(1201, 529)
        mbta_tracker_window.setStyleSheet("background-color: #547A6D; color: #FAF9F6;")
        self.title_label = QtWidgets.QLabel(mbta_tracker_window)
        self.title_label.setGeometry(QtCore.QRect(30, 20, 391, 71))
        font = QtGui.QFont()
        font.setFamily("Source Serif Pro Black")
        font.setPointSize(32)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.title_label.setFont(font)
        self.title_label.setObjectName("title_label")
        self.ride_1 = QtWidgets.QGroupBox(mbta_tracker_window)
        self.ride_1.setGeometry(QtCore.QRect(20, 330, 381, 181))
        font = QtGui.QFont()
        font.setFamily("Source Serif Pro Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.ride_1.setFont(font)
        self.ride_1.setObjectName("ride_1")
        self.ride_1_box_1 = QtWidgets.QPlainTextEdit(self.ride_1)
        self.ride_1_box_1.setGeometry(QtCore.QRect(20, 30, 341, 61))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.ride_1_box_1.setFont(font)
        self.ride_1_box_1.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.ride_1_box_1.setStyleSheet("background-color: black; color: #FFC600;")
        self.ride_1_box_1.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.ride_1_box_1.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.ride_1_box_1.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.ride_1_box_1.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.ride_1_box_1.setLineWrapMode(QtWidgets.QPlainTextEdit.LineWrapMode.WidgetWidth)
        self.ride_1_box_1.setReadOnly(True)
        self.ride_1_box_1.setPlainText("")
        self.ride_1_box_1.setObjectName("ride_1_box_1")
        self.ride_1_box_2 = QtWidgets.QPlainTextEdit(self.ride_1)
        self.ride_1_box_2.setGeometry(QtCore.QRect(20, 100, 341, 61))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.ride_1_box_2.setFont(font)
        self.ride_1_box_2.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.ride_1_box_2.setStyleSheet("background-color: black; color: #FFC600;")
        self.ride_1_box_2.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.ride_1_box_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.ride_1_box_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.ride_1_box_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.ride_1_box_2.setLineWrapMode(QtWidgets.QPlainTextEdit.LineWrapMode.WidgetWidth)
        self.ride_1_box_2.setReadOnly(True)
        self.ride_1_box_2.setPlainText("")
        self.ride_1_box_2.setObjectName("ride_1_box_2")
        self.ride_2 = QtWidgets.QGroupBox(mbta_tracker_window)
        self.ride_2.setGeometry(QtCore.QRect(410, 330, 381, 181))
        font = QtGui.QFont()
        font.setFamily("Source Serif Pro Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.ride_2.setFont(font)
        self.ride_2.setObjectName("ride_2")
        self.ride_2_box_2 = QtWidgets.QPlainTextEdit(self.ride_2)
        self.ride_2_box_2.setGeometry(QtCore.QRect(20, 100, 341, 61))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.ride_2_box_2.setFont(font)
        self.ride_2_box_2.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.ride_2_box_2.setStyleSheet("background-color: black; color: #FFC600;")
        self.ride_2_box_2.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.ride_2_box_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.ride_2_box_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.ride_2_box_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.ride_2_box_2.setLineWrapMode(QtWidgets.QPlainTextEdit.LineWrapMode.WidgetWidth)
        self.ride_2_box_2.setReadOnly(True)
        self.ride_2_box_2.setPlainText("")
        self.ride_2_box_2.setObjectName("ride_2_box_2")
        self.ride_2_box_1 = QtWidgets.QPlainTextEdit(self.ride_2)
        self.ride_2_box_1.setGeometry(QtCore.QRect(20, 30, 341, 61))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.ride_2_box_1.setFont(font)
        self.ride_2_box_1.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.ride_2_box_1.setStyleSheet("background-color: black; color: #FFC600;")
        self.ride_2_box_1.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.ride_2_box_1.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.ride_2_box_1.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.ride_2_box_1.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.ride_2_box_1.setLineWrapMode(QtWidgets.QPlainTextEdit.LineWrapMode.WidgetWidth)
        self.ride_2_box_1.setReadOnly(True)
        self.ride_2_box_1.setPlainText("")
        self.ride_2_box_1.setObjectName("ride_2_box_1")
        self.ride_3 = QtWidgets.QGroupBox(mbta_tracker_window)
        self.ride_3.setGeometry(QtCore.QRect(800, 330, 381, 181))
        font = QtGui.QFont()
        font.setFamily("Source Serif Pro Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.ride_3.setFont(font)
        self.ride_3.setObjectName("ride_3")
        self.ride_3_box_2 = QtWidgets.QPlainTextEdit(self.ride_3)
        self.ride_3_box_2.setGeometry(QtCore.QRect(20, 100, 341, 61))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.ride_3_box_2.setFont(font)
        self.ride_3_box_2.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.ride_3_box_2.setStyleSheet("background-color: black; color: #FFC600;")
        self.ride_3_box_2.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.ride_3_box_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.ride_3_box_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.ride_3_box_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.ride_3_box_2.setLineWrapMode(QtWidgets.QPlainTextEdit.LineWrapMode.WidgetWidth)
        self.ride_3_box_2.setReadOnly(True)
        self.ride_3_box_2.setPlainText("")
        self.ride_3_box_2.setObjectName("ride_3_box_2")
        self.ride_3_box_1 = QtWidgets.QPlainTextEdit(self.ride_3)
        self.ride_3_box_1.setGeometry(QtCore.QRect(20, 30, 341, 61))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.ride_3_box_1.setFont(font)
        self.ride_3_box_1.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.ride_3_box_1.setStyleSheet("background-color: black; color: #FFC600;")
        self.ride_3_box_1.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.ride_3_box_1.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.ride_3_box_1.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.ride_3_box_1.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.ride_3_box_1.setLineWrapMode(QtWidgets.QPlainTextEdit.LineWrapMode.WidgetWidth)
        self.ride_3_box_1.setReadOnly(True)
        self.ride_3_box_1.setPlainText("")
        self.ride_3_box_1.setObjectName("ride_3_box_1")
        self.trip_selector = QtWidgets.QGroupBox(mbta_tracker_window)
        self.trip_selector.setGeometry(QtCore.QRect(20, 110, 1161, 201))
        font = QtGui.QFont()
        font.setFamily("Source Serif Pro Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.trip_selector.setFont(font)
        self.trip_selector.setObjectName("trip_selector")
        self.method_box = QtWidgets.QComboBox(self.trip_selector)
        self.method_box.setGeometry(QtCore.QRect(890, 70, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.method_box.setFont(font)
        self.method_box.setStyleSheet("background-color: #FAF9F6; color: black;")
        self.method_box.setObjectName("method_box")
        self.stop_box = QtWidgets.QComboBox(self.trip_selector)
        self.stop_box.setGeometry(QtCore.QRect(310, 70, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.stop_box.setFont(font)
        self.stop_box.setStyleSheet("background-color: #FAF9F6; color: black;")
        self.stop_box.setObjectName("stop_box")
        self.direction_box = QtWidgets.QComboBox(self.trip_selector)
        self.direction_box.setGeometry(QtCore.QRect(600, 70, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.direction_box.setFont(font)
        self.direction_box.setAutoFillBackground(False)
        self.direction_box.setStyleSheet("background-color: #FAF9F6; color: black;")
        self.direction_box.setObjectName("direction_box")
        self.route_box = QtWidgets.QComboBox(self.trip_selector)
        self.route_box.setGeometry(QtCore.QRect(20, 70, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.route_box.setFont(font)
        self.route_box.setStyleSheet("background-color: #FAF9F6; color: black;")
        self.route_box.setEditable(False)
        self.route_box.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.route_box.setObjectName("route_box")
        self.display_button = QtWidgets.QPushButton(self.trip_selector)
        self.display_button.setGeometry(QtCore.QRect(170, 140, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Source Serif Pro Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.display_button.setFont(font)
        self.display_button.setObjectName("display_button")
        self.favorites_button = QtWidgets.QPushButton(self.trip_selector)
        self.favorites_button.setGeometry(QtCore.QRect(460, 140, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Source Serif Pro Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.favorites_button.setFont(font)
        self.favorites_button.setObjectName("favorites_button")
        self.restore_button = QtWidgets.QPushButton(self.trip_selector)
        self.restore_button.setGeometry(QtCore.QRect(750, 140, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Source Serif Pro Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.restore_button.setFont(font)
        self.restore_button.setStyleSheet("background-color: #588577;")
        self.restore_button.setFlat(False)
        self.restore_button.setObjectName("restore_button")
        self.route_label = QtWidgets.QLabel(self.trip_selector)
        self.route_label.setGeometry(QtCore.QRect(20, 42, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Source Serif Pro Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.route_label.setFont(font)
        self.route_label.setObjectName("route_label")
        self.stop_label = QtWidgets.QLabel(self.trip_selector)
        self.stop_label.setGeometry(QtCore.QRect(310, 40, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Source Serif Pro Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.stop_label.setFont(font)
        self.stop_label.setObjectName("stop_label")
        self.direction_label = QtWidgets.QLabel(self.trip_selector)
        self.direction_label.setGeometry(QtCore.QRect(600, 32, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Source Serif Pro Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.direction_label.setFont(font)
        self.direction_label.setObjectName("direction_label")
        self.method_label = QtWidgets.QLabel(self.trip_selector)
        self.method_label.setGeometry(QtCore.QRect(890, 40, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Source Serif Pro Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.method_label.setFont(font)
        self.method_label.setObjectName("method_label")
        self.label = QtWidgets.QLabel(self.trip_selector)
        self.label.setGeometry(QtCore.QRect(890, 110, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Source Serif Pro Black")
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #DFDFDF")
        self.label.setObjectName("label")
        self.route_label.raise_()
        self.stop_label.raise_()
        self.direction_label.raise_()
        self.method_label.raise_()
        self.direction_box.raise_()
        self.route_box.raise_()
        self.display_button.raise_()
        self.favorites_button.raise_()
        self.stop_box.raise_()
        self.label.raise_()
        self.restore_button.raise_()
        self.method_box.raise_()
        self.refresh_lcd = QtWidgets.QLCDNumber(mbta_tracker_window)
        self.refresh_lcd.setGeometry(QtCore.QRect(1130, 40, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.refresh_lcd.setFont(font)
        self.refresh_lcd.setStyleSheet("background-color: black; color: #BD3039;; border-color: black;")
        self.refresh_lcd.setDigitCount(2)
        self.refresh_lcd.setSegmentStyle(QtWidgets.QLCDNumber.SegmentStyle.Flat)
        self.refresh_lcd.setObjectName("refresh_lcd")
        self.refreshes_in = QtWidgets.QLabel(mbta_tracker_window)
        self.refreshes_in.setGeometry(QtCore.QRect(890, 40, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Source Serif Pro Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.refreshes_in.setFont(font)
        self.refreshes_in.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.refreshes_in.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.refreshes_in.setObjectName("refreshes_in")
        self.ride_1.raise_()
        self.trip_selector.raise_()
        self.ride_3.raise_()
        self.ride_2.raise_()
        self.title_label.raise_()
        self.refreshes_in.raise_()
        self.refresh_lcd.raise_()

        self.retranslateUi(mbta_tracker_window)
        QtCore.QMetaObject.connectSlotsByName(mbta_tracker_window)

    def retranslateUi(self, mbta_tracker_window):
        _translate = QtCore.QCoreApplication.translate
        mbta_tracker_window.setWindowTitle(_translate("mbta_tracker_window", "MBTA Ride Tracker by Drew Bowler"))
        self.title_label.setText(_translate("mbta_tracker_window", "MBTA Ride Tracker"))
        self.ride_1.setTitle(_translate("mbta_tracker_window", "Ride 1"))
        self.ride_2.setTitle(_translate("mbta_tracker_window", "Ride 2"))
        self.ride_3.setTitle(_translate("mbta_tracker_window", "Ride 3"))
        self.trip_selector.setTitle(_translate("mbta_tracker_window", "Trip Selector"))
        self.display_button.setStyleSheet(_translate("mbta_tracker_window", "background-color: #588577;"))
        self.display_button.setText(_translate("mbta_tracker_window", "Display Rides"))
        self.favorites_button.setStyleSheet(_translate("mbta_tracker_window", "background-color: #588577;"))
        self.favorites_button.setText(_translate("mbta_tracker_window", "Save Current Rides"))
        self.restore_button.setText(_translate("mbta_tracker_window", "Load Saved Rides"))
        self.route_label.setText(_translate("mbta_tracker_window", "Route"))
        self.stop_label.setText(_translate("mbta_tracker_window", "Stop"))
        self.direction_label.setText(_translate("mbta_tracker_window", "Direction"))
        self.method_label.setText(_translate("mbta_tracker_window", "Method"))
        self.label.setText(_translate("mbta_tracker_window", "For stops at the end of a route, use \"Schedules\""))
        self.refreshes_in.setText(_translate("mbta_tracker_window", "Refreshes in:"))
