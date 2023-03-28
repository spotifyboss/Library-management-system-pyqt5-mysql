from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice
from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtCore import Qt
import mysql.connector
import random

# For getting random colors
hexadecimal = "#" + ''.join([random.choice('ABCDEF0123456789') for i in range(6)])

db = mysql.connector.connect(
    host="sql7.freemysqlhosting.net",
    user="sql7609276",
    passwd="ppKwkNQ2NW",
    database="sql7609276"
)

cursor = db.cursor()

cursor.execute("SELECT country,count(*) FROM customers GROUP BY country ORDER BY count(*) DESC")


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQtChart Pie Chart")
        self.setGeometry(100, 100, 1280, 600)

        self.show()

        self.create_piechart()

    def create_piechart(self):
        series = QPieSeries()
        slice = QPieSlice()
        y = 0
        for x in cursor:
            print(x)
            print(y)
            series.append(x[0], x[1])
            slice = series.slices()[y]
            slice.setPen(QPen(Qt.black, 2))
            slice.setBrush(QColor("#" + ''.join([random.choice('ABCDEF0123456789') for i in range(6)])))
            y += 1

        chart = QChart()
        chart.legend().hide()
        chart.addSeries(series)
        chart.createDefaultAxes()
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTitle("Pie Chart Example")

        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

        chartview = QChartView(chart)
        chartview.setRenderHint(QPainter.Antialiasing)

        self.setCentralWidget(chartview)


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())
