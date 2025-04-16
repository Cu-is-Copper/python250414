import random
from openpyxl import Workbook

# 전자제품 이름 리스트
product_names = [
    "Smartphone", "Laptop", "Tablet", "Smartwatch", "Headphones",
    "Bluetooth Speaker", "Camera", "Printer", "Monitor", "Keyboard",
    "Mouse", "Router", "External Hard Drive", "USB Flash Drive", "Power Bank",
    "Gaming Console", "Drone", "Projector", "Smart TV", "Fitness Tracker"
]

# 엑셀 파일 생성
wb = Workbook()
ws = wb.active
ws.title = "제품리스트"

# 헤더 추가
ws.append(["Product ID", "Product Name", "Quantity", "Price"])

# 데이터 생성 및 추가
for i in range(1, 101):  # 100개의 데이터 생성
    product_id = f"P{i:03d}"  # P001, P002 형식의 ID
    product_name = random.choice(product_names)
    quantity = random.randint(1, 100)  # 1~100 사이의 수량
    price = round(random.uniform(100, 10000), 2)  # 10.0~1000.0 사이의 가격
    ws.append([product_id, product_name, quantity, price])

# 엑셀 파일 저장
wb.save("products.xlsx")
print("products.xlsx 파일이 생성되었습니다.")