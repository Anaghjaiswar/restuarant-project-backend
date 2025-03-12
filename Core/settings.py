from pathlib import Path
import os
import dj_database_url
from decouple import config
from dotenv import load_dotenv
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET_KEY')

DEBUG = config("DEBUG", cast=bool)

ALLOWED_HOSTS = config("ALLOWED_HOSTS").split(",")


INSTALLED_APPS = [
    'jazzmin',
    # 'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary',
    'cloudinary_storage',
    'Menu',
    'rest_framework',
    'corsheaders',
    'Contact',
    'GiftVouchers',
    'BookTable',
]

CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:5500",
    "https://anaghjaiswar.github.io",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'Core.wsgi.application'

# Render's postgre sql configuration
DATABASES = {
    'default': dj_database_url.config(default=os.getenv('DATABASE_URL')),
    'custom1':{
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}



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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True
STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# jazzmin settings
JAZZMIN_SETTINGS = {
    "site_title": "Pro Admin Panel",
    "site_header": "Pro Admin Dashboard",
    "welcome_sign": "Welcome to the Pro Admin Dashboard",
    "copyright": "Pro Admin 2024",
    "search_model": "auth.User",  # Search bar for a specific model
    "user_avatar": None,  # Add user profile picture if available
    "topmenu_links": [
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "Support", "url": "https://example.com/support", "new_window": True},
    ],
    "show_sidebar": True,
    "navigation_expanded": True,
    "hide_apps": ["sessions"],  # Hide specific apps from the sidebar
    "hide_models": ["auth.Group"],  # Hide specific models
    "order_with_respect_to": ["auth", "app_name.ModelName"],  # Custom app order
    "icons": {
        "auth": "fas fa-users",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users-cog",
    },
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
    "related_modal_active": True,
    "custom_css": None,  # Add path to custom CSS file
    "custom_js": None,  # Add path to custom JS file
    "show_ui_builder": True,  # Enable/Disable UI builder in the admin
}


# Email configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


# CLOUDINARY CONFIGURATION
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.getenv('CLOUDINARY_CLOUD_NAME'),
    'API_KEY': os.getenv('CLOUDINARY_API_KEY'),
    'API_SECRET': os.getenv('CLOUDINARY_API_SECRET'),
}
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# razorpay configuration
# settings.py
RAZORPAY_KEY_ID = os.getenv('RAZORPAY_KEY_ID')
RAZORPAY_KEY_SECRET = os.getenv('RAZORPAY_KEY_SECRET')
