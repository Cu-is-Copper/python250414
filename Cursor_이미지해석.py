import sys
import base64
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import openai
from pathlib import Path

class DemoForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()
        
    def setupUI(self):
        # 윈도우 설정
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle("이미지 해석 프로그램")

        # 중앙 위젯 설정
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        layout = QVBoxLayout(centralWidget)

        # 이미지 표시 레이블
        self.imageLabel = QLabel()
        self.imageLabel.setFixedSize(500, 400)
        self.imageLabel.setAlignment(Qt.AlignCenter)
        self.imageLabel.setStyleSheet("border: 2px solid black")
        layout.addWidget(self.imageLabel)

        # 결과 표시 텍스트 영역
        self.resultText = QTextEdit()
        self.resultText.setFixedHeight(100)
        self.resultText.setReadOnly(True)
        layout.addWidget(self.resultText)

        # 버튼 영역
        buttonLayout = QHBoxLayout()
        
        self.selectButton = QPushButton("이미지 선택")
        self.selectButton.clicked.connect(self.selectImage)
        buttonLayout.addWidget(self.selectButton)

        self.analyzeButton = QPushButton("이미지 분석")
        self.analyzeButton.clicked.connect(self.analyzeImage)
        self.analyzeButton.setEnabled(False)
        buttonLayout.addWidget(self.analyzeButton)

        layout.addLayout(buttonLayout)

        # OpenAI API 키 입력
        keyLayout = QHBoxLayout()
        keyLayout.addWidget(QLabel("OpenAI API Key:"))
        self.apiKeyInput = QLineEdit()
        self.apiKeyInput.setEchoMode(QLineEdit.Password)
        keyLayout.addWidget(self.apiKeyInput)
        layout.addLayout(keyLayout)

        self.selected_image_path = None

    def selectImage(self):
        fname, _ = QFileDialog.getOpenFileName(self, '이미지 선택', '', 
            'Image files (*.jpg *.jpeg *.png *.bmp *.gif)')
        
        if fname:
            self.selected_image_path = fname
            pixmap = QPixmap(fname)
            scaled_pixmap = pixmap.scaled(500, 400, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.imageLabel.setPixmap(scaled_pixmap)
            self.analyzeButton.setEnabled(True)

    def analyzeImage(self):
        if not self.selected_image_path or not self.apiKeyInput.text():
            QMessageBox.warning(self, '경고', 'API 키와 이미지를 모두 선택해주세요.')
            return

        try:
            # API 키 설정
            openai.api_key = self.apiKeyInput.text()

            # 이미지를 base64로 인코딩
            with open(self.selected_image_path, "rb") as image_file:
                base64_image = base64.b64encode(image_file.read()).decode('utf-8')

            # OpenAI API 호출
            response = openai.ChatCompletion.create(
                model="gpt-4-vision-preview",
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": "이 이미지에 대해 자세히 설명해주세요."},
                            {
                                "type": "image_url",
                                "image_url": f"data:image/jpeg;base64,{base64_image}"
                            }
                        ]
                    }
                ],
                max_tokens=500
            )

            # 결과 표시
            result = response.choices[0].message.content
            self.resultText.setText(result)

        except Exception as e:
            QMessageBox.critical(self, '오류', f'이미지 분석 중 오류가 발생했습니다: {str(e)}')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = DemoForm()
    demo.show()
    app.exec_()
