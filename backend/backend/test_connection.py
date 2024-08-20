from djongo import models

try:
    # Tạo một model đơn giản để kiểm tra kết nối
    class TestModel(models.Model):
        name = models.CharField(max_length=100)
    
    # Lưu một instance của TestModel
    TestModel(name="Test").save()
    
    print("Kết nối với MongoDB thành công!")
except Exception as e:
    print(f"Lỗi khi kết nối với MongoDB: {e}")