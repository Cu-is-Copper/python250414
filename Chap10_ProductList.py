import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5 import uic
import sqlite3
import os.path

class DatabaseManager:
    def __init__(self, db_name="ProductList.db"):
        self.db_name = db_name
        self.con = None
        self.cur = None
        self._connect()

    def _connect(self):
        """Connect to the database and create the table if it doesn't exist."""
        self.con = sqlite3.connect(self.db_name)
        self.cur = self.con.cursor()
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS Products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                Name TEXT,
                Price INTEGER
            );
        """)

    def execute_query(self, query, params=()):
        """Execute a query with optional parameters."""
        self.cur.execute(query, params)
        self.con.commit()

    def fetch_all(self, query, params=()):
        """Fetch all rows for a given query."""
        self.cur.execute(query, params)
        return self.cur.fetchall()

    def close(self):
        """Close the database connection."""
        if self.con:
            self.con.close()


# 디자인 파일 로딩
form_class = uic.loadUiType("Chap10_ProductList.ui")[0]

class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Database Manager 초기화
        self.db_manager = DatabaseManager()

        # 초기값 셋팅
        self.id = 0
        self.name = ""
        self.price = 0

        # QTableWidget 설정
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setHorizontalHeaderLabels(["제품ID", "제품명", "가격"])
        self.tableWidget.setTabKeyNavigation(False)
        self.tableWidget.doubleClicked.connect(self.doubleClick)

        # 버튼 연결
        self.pushButton.clicked.connect(self.addProduct)
        self.pushButton_2.clicked.connect(self.updateProduct)
        self.pushButton_3.clicked.connect(self.removeProduct)
        self.pushButton_4.clicked.connect(self.getProduct)

    def addProduct(self):
        """Add a new product to the database."""
        self.name = self.prodName.text().strip()  # 공백 제거
        self.price = self.prodPrice.text().strip()  # 공백 제거

        # 입력값 검증
        if not self.name:
            QMessageBox.warning(self, "입력 오류", "제품명을 입력하세요.")
            return

        if not self.price.isdigit():
            QMessageBox.warning(self, "입력 오류", "가격은 숫자로 입력하세요.")
            return

        # 데이터베이스에 제품 추가
        self.db_manager.execute_query(
            "INSERT INTO Products (Name, Price) VALUES (?, ?);",
            (self.name, int(self.price))
        )

        # 입력 필드 초기화
        self.prodName.clear()
        self.prodPrice.clear()

        # 테이블 갱신
        self.getProduct()

    def updateProduct(self):
        """Update an existing product in the database."""
        self.id = self.prodID.text()
        self.name = self.prodName.text()
        self.price = self.prodPrice.text()
        if self.id.isdigit() and self.name and self.price.isdigit():
            self.db_manager.execute_query(
                "UPDATE Products SET Name = ?, Price = ? WHERE id = ?;",
                (self.name, int(self.price), int(self.id))
            )
            self.getProduct()
        else:
            QMessageBox.warning(self, "입력 오류", "올바른 데이터를 입력하세요.")

    def removeProduct(self):
        """Remove a product from the database."""
        self.id = self.prodID.text()
        if self.id.isdigit():
            self.db_manager.execute_query(
                "DELETE FROM Products WHERE id = ?;",
                (int(self.id),)
            )
            self.getProduct()
        else:
            QMessageBox.warning(self, "입력 오류", "올바른 제품 ID를 입력하세요.")

    def getProduct(self):
        """Retrieve and display all products from the database."""
        self.tableWidget.clearContents()
        products = self.db_manager.fetch_all("SELECT * FROM Products;")
        self.tableWidget.setRowCount(len(products))

        for row, item in enumerate(products):
            itemID = QTableWidgetItem(str(item[0]))
            itemID.setTextAlignment(Qt.AlignRight)
            self.tableWidget.setItem(row, 0, itemID)

            self.tableWidget.setItem(row, 1, QTableWidgetItem(item[1]))

            itemPrice = QTableWidgetItem(str(item[2]))
            itemPrice.setTextAlignment(Qt.AlignRight)
            self.tableWidget.setItem(row, 2, itemPrice)

    def doubleClick(self):
        """Handle double-click events on the table."""
        self.prodID.setText(self.tableWidget.item(self.tableWidget.currentRow(), 0).text())
        self.prodName.setText(self.tableWidget.item(self.tableWidget.currentRow(), 1).text())
        self.prodPrice.setText(self.tableWidget.item(self.tableWidget.currentRow(), 2).text())

    def closeEvent(self, event):
        """Ensure the database connection is closed when the application exits."""
        self.db_manager.close()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoForm = DemoForm()
    demoForm.show()
    app.exec_()




