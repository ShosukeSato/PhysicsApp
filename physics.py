import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QComboBox, QMessageBox

# 計算関数の定義
def calculate_velocity(distance, time):
    return distance / time if time != 0 else 'Error'

def calculate_acceleration(velocity, time):
    return velocity / time if time != 0 else 'Error'

def calculate_force(mass, acceleration):
    return mass * acceleration

# メインウィンドウのクラス
class PhysicsCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Physics Calculator")
        self.layout = QVBoxLayout(self)

        # コンボボックスで計算する物理量を選択
        self.comboBox = QComboBox(self)
        self.comboBox.addItems(["Velocity", "Acceleration", "Force"])
        self.comboBox.currentIndexChanged.connect(self.updatePlaceholders)
        self.layout.addWidget(self.comboBox)

        # 入力フィールド
        self.input1 = QLineEdit(self)
        self.layout.addWidget(self.input1)
        self.input2 = QLineEdit(self)
        self.layout.addWidget(self.input2)
        self.updatePlaceholders(0)  # 初期プレースホルダーの設定

        # 計算ボタン
        self.calcButton = QPushButton("Calculate")
        self.calcButton.clicked.connect(self.calculate)
        self.layout.addWidget(self.calcButton)

        # 結果表示ラベル
        self.resultLabel = QLabel("")
        self.layout.addWidget(self.resultLabel)

    def updatePlaceholders(self, index):
        if index == 0:  # Velocity
            self.input1.setPlaceholderText("Distance (m)")
            self.input2.setPlaceholderText("Time (s)")
        elif index == 1:  # Acceleration
            self.input1.setPlaceholderText("Velocity (m/s)")
            self.input2.setPlaceholderText("Time (s)")
        else:  # Force
            self.input1.setPlaceholderText("Mass (kg)")
            self.input2.setPlaceholderText("Acceleration (m/s²)")

    def calculate(self):
        try:
            value1 = float(self.input1.text())
            value2 = float(self.input2.text())
            selection = self.comboBox.currentText()

            if selection == "Velocity":
                result = calculate_velocity(value1, value2)
                unit = "m/s"
            elif selection == "Acceleration":
                result = calculate_acceleration(value1, value2)
                unit = "m/s²"
            else:  # Force
                result = calculate_force(value1, value2)
                unit = "N"  # ニュートン

            self.resultLabel.setText(f"Result: {result} {unit}")
        except ValueError:
            QMessageBox.warning(self, "Error", "Invalid input")


# アプリケーションの実行
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PhysicsCalculator()
    ex.show()
    sys.exit(app.exec())
