from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class MyAccountManager(BaseUserManager):
    # 일반 user 생성, username 이 userID를 의미함
    def create_user(self, username, email, nickname, password=None):
        if not username:
            raise ValueError("Users must have an userID.")
        if not email:
            raise ValueError("Users must have an email.")
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            nickname=nickname
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    # 관리자 User 생성
    def create_superuser(self, username, email, nickname, password, **extra_fields):
        user = self.create_user(
            username=username,
            email=email,
            nickname=nickname,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=30, unique=True, default='crawling')
    email = models.EmailField(max_length=100, unique=True, default='crawling@email.com')
    nickname = models.CharField(max_length=30, unique=True, default='crawling')
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    object = MyAccountManager()  # 헬퍼 클래스 사용

    USERNAME_FIELD = 'username'  # 로그인 ID로 사용할 필드
    REQUIRED_FIELDS = ['email','nickname']  # 필수 작성 필드

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_lable):
        return True
