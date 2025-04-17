import sys
import base64
import requests
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QFileDialog, QVBoxLayout, QWidget, QTextEdit
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class DemoForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("이미지 해석 애플리케이션")
        self.setGeometry(100, 100, 800, 800)

        # 중앙 위젯 및 레이아웃 설정
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # 이미지 표시 라벨
        self.image_label = QLabel("이미지를 선택하세요")
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setFixedSize(600, 400)
        self.layout.addWidget(self.image_label)

        # 결과 표시를 위한 텍스트 에디터
        self.result_text = QTextEdit()
        self.result_text.setFixedHeight(200)
        self.result_text.setReadOnly(True)
        self.layout.addWidget(self.result_text)

        # 버튼 영역
        self.select_button = QPushButton("이미지 선택")
        self.select_button.clicked.connect(self.select_image)
        self.layout.addWidget(self.select_button)

        self.analyze_button = QPushButton("이미지 분석")
        self.analyze_button.clicked.connect(self.analyze_image)
        self.layout.addWidget(self.analyze_button)

        self.image_path = None

    def select_image(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, 
            "이미지 선택", 
            "", 
            "Images (*.png *.jpg *.jpeg *.bmp)"
        )
        if file_path:
            self.image_path = file_path
            pixmap = QPixmap(file_path)
            scaled_pixmap = pixmap.scaled(
                self.image_label.size(), 
                Qt.KeepAspectRatio, 
                Qt.SmoothTransformation
            )
            self.image_label.setPixmap(scaled_pixmap)

    def analyze_image(self):
        if not self.image_path:
            self.result_text.setText("이미지를 먼저 선택하세요.")
            return

        try:
            # 이미지를 base64로 인코딩
            with open(self.image_path, "rb") as image_file:
                encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

            # OpenAI API 설정
            api_key = os.getenv("OPENAI_API_KEY")
            if not api_key:
                self.result_text.setText("OpenAI API 키가 설정되지 않았습니다.")
                return

            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            }

            data = {
                "model": "gpt-4o",
                "messages": [
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": "이 이미지를 자세히 설명해주세요."},
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/jpeg;base64,{encoded_image}"
                                }
                            }
                        ]
                    }
                ],
                "max_tokens": 500
            }

            self.result_text.setText("분석 중...")
            response = requests.post(
                "https://api.openai.com/v1/chat/completions",
                headers=headers,
                json=data
            )

            if response.status_code == 200:
                result = response.json()
                description = result['choices'][0]['message']['content']
                self.result_text.setText(description)
            else:
                self.result_text.setText(f"API 호출 실패 (코드: {response.status_code})\n{response.text}")

        except Exception as e:
            self.result_text.setText(f"오류 발생: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = DemoForm()
    demo.show()
    sys.exit(app.exec_())