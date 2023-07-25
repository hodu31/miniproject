"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-6u&m6+-e%61-ba)d96whm)x-ks&r6jhe37tt%+)jml4&y8=waz'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

### 수정
ALLOWED_HOSTS = ['127.0.0.1']

# Application definition

### 새로운 앱이 생성되면 이곳에 등록해 주기...
INSTALLED_APPS = [
    'nonmodelapp',
    'frontapp',
    'mainapp',
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

### 내 서버내에서 iframe 적용하기
X_FRAME_OPTIONS = "SAMEORIGIN"

### iframe 적용 안하기
# X_FRAME_OPTIONS = "DENY"

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    ### 오라클 사용시 추가
    'oracle' : {
        'ENGINE' : 'django.db.backends.oracle',
        'NAME' : 'xe',
        'USER' : 'minipro',
        'PASSWORD' : 'dbdb',
        'HOST' : 'localhost',
        'PORT' : '1521',
    },
}

### 추가된 DB를 사용할 app을 지정(연결)하기
DATABASE_ROUTERS = [
    ### 앱이름.router파일이름.클래스이름(클래스이름은 바뀔수 있음)
    # 예시 : 'firstapp.router.DBRouter',
    'oracleapp.router.DBRouter',
    'mainapp.router.DBRouter',
]

### Logging 처리
# - DB 실행 내용을 console 창에서 확인할 수 있도록 처리
LOGGING = {
    'version':1,
    'disable_existing_loggers':False,
    'handlers':{
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
        }
    },
    'loggers':{
        'django.db.backends':{
            'handlers':['console'],
            'level':'DEBUG',
        }
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

### 한글언어로 수정
# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'ko-kr'

### 시간대를 아시아/서울 시간대로 수정
# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

### 정적파일을 관리하는 경로 
# - 정적파일 : css, javascript, 이미지, 동영상 등등(html은 제외)
STATIC_URL = 'static/'

### 추가 사항
### 각 앱(app)에서 관리할 수 있도록 정적파일 관리 폴더 정의하기
STATICFILES_DIRS = [BASE_DIR/'static']

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


### 로그인 상태에서 브라우저가 닫혔을 때 
# - 세션정보(로그인 정보) 삭제하기(로그아웃 처리)
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
