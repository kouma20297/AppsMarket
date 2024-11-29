from django.db import models
from django.utils.timezone  import now

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    last_name = models.CharField(max_length=100, default='Unknown')  # デフォルト値を追加
    first_name = models.CharField(max_length=100, default='Unknown')  # デフォルト値を追加
    phone_number = models.CharField(max_length=15, unique=True)
    password_hash = models.CharField(max_length=255, default='')  # デフォルト値を追加
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user'
        verbose_name = "User"


    def __str__(self):
        return f"ID: {self.user_id}, Email: {self.email}"
