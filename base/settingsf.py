"""
Django settings for base project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

from django.contrib import admin

from base import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-q8h&6jj@l1v$t$$q%jl=$y2j-08nxptg1r0@z2m(qd(semll98"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    "127.0.0.1",
    "top25index.com",
    "www.top25index.com",
    "top25restaurants.com",
    "www.top25restaurants.com",
]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
    "ckeditor",
    "ckeditor_uploader",
    "crispy_forms",
    "crispy_bootstrap5",
    "captcha",
    "easy_thumbnails",
    "filer",
    "mptt",
    "import_export",
    "tinymce",
    "accounts.apps.AccountsConfig",
    "pages_app.apps.PagesAppConfig",
    "interests.apps.InterestsConfig",
    "list.apps.ListConfig",
    "mailing.apps.MailingConfig",
    "filters.apps.FiltersConfig",
]

SITE_ID = 1

AUTH_USER_MODEL = "accounts.User"

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_USERNAME_MIN_LENGTH = 6
ACCOUNT_USERNAME_BLACKLIST = ["home", "index", "admin", "info", "top25", "backup"]
SOCIALACCOUNT_AUTO_SIGNUP = False
LOGIN_REDIRECT_URL = "/profile/"
LOGIN_URL = "/login/"

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
]

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.mailersend.net"
EMAIL_PORT = "587"
EMAIL_HOST_USER = "MS_BnamXw@top25restaurants.com"
EMAIL_HOST_PASSWORD = "85V7rSWJeW5Ygrry"
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = "noreply@top25restaurants.com"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# CACHES = {
#     "default": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": "redis://127.0.0.1:6379/1",
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",
#         }
#     }
# }


ROOT_URLCONF = "base.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "pages_app.context_processors.base_variable",
            ],
        },
    },
]

WSGI_APPLICATION = "base.wsgi.application"


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# django-filer
THUMBNAIL_PROCESSORS = (
    "easy_thumbnails.processors.colorspace",
    "easy_thumbnails.processors.autocrop",
    #'easy_thumbnails.processors.scale_and_crop',
    "filer.thumbnail_processors.scale_and_crop_with_subject_location",
    "easy_thumbnails.processors.filters",
)
FILER_STORAGES = {
    "public": {
        "main": {
            "UPLOAD_TO": "my_filer.generate_filer_filename.custom_filename",
            "UPLOAD_TO_PREFIX": "img",
        },
        "thumbnails": {
            "THUMBNAIL_OPTIONS": {
                "base_dir": "thumbnails",
            },
        },
    },
}


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# ckeditor
CKEDITOR_CONFIGS = {
    "default": {
        "toolbar": [
            ["Format", "Bold", "Italic", "Underline", "Strike", "SpellChecker"],
            [
                "NumberedList",
                "BulletedList",
                "Indent",
                "Outdent",
                "JustifyLeft",
                "JustifyCenter",
                "JustifyRight",
                "JustifyBlock",
            ],
            [
                "Image",
                "Table",
                "Link",
                "Unlink",
                "Anchor",
                "SectionLink",
                "Subscript",
                "Superscript",
            ],
            ["Undo", "Redo"],
            ["Source"],
            ["Maximize"],
        ],
        "allowedContent": True,
        "height": "250px",
        "width": "full",
    },
    "interest_form": {
        "toolbar": [
            ["Format", "Bold", "Italic", "Underline", "Strike", "SpellChecker"],
            [
                "NumberedList",
                "BulletedList",
                "Indent",
                "Outdent",
                "JustifyLeft",
                "JustifyCenter",
                "JustifyRight",
                "JustifyBlock",
            ],
            [
                "Image",
                "Table",
                "Link",
                "Unlink",
                "Anchor",
                "SectionLink",
                "Subscript",
                "Superscript",
            ],
            ["Undo", "Redo"],
            ["Source"],
            ["Maximize"],
        ],
        "allowedContent": True,
        "height": "250px",
        "width": "full",
        "editorplaceholder": config.PLACEHOLDER_TEXT,
    },
}

CKEDITOR_UPLOAD_PATH = "ckupload/"

# bootstrap
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"


# Admin Ordering
ADMIN_ORDERING = [
    (
        "interests",
        [
            "Region",
            "ReviewAndRating",
            "Comment",
            "Interest",
        ],
    ),
    (
        "pages_app",
        [
            "ContentPage",
            "Navbar",
            "Footer",
            "Sidebar",
            "Script",
        ],
    ),
    (
        "filters",
        [
            "Filter",
        ],
    ),
    (
        "mailing",
        [
            "ContactEntry",
            "Subscriber",
        ],
    ),
    (
        "list",
        [
            "Autoblogging",
            "Category",
            "Post",
            "Billboard",
            "Tag",
        ],
    ),
    (
        "account",
        [
            "EmailAddress",
        ],
    ),
    (
        "accounts",
        [
            "Profile",
            "User",
        ],
    ),
    (
        "auth",
        [
            "Group",
        ],
    ),
    (
        "sites",
        [
            "Site",
        ],
    ),
    (
        "socialaccount",
        [
            "SocialAccount",
            "SocialToken",
            "SocialApp",
        ],
    ),
]


# Creating a sort function
def get_app_list(self, request):
    app_dict = self._build_app_dict(request)
    for app_name, object_list in ADMIN_ORDERING:
        try:
            app = app_dict[app_name]
            app["models"].sort(key=lambda x: object_list.index(x["object_name"]))
            yield app
        except:
            print()


# Covering django.contrib.admin.AdminSite.get_app_list
admin.AdminSite.get_app_list = get_app_list


# Settings for django-simple-captcha
CAPTCHA_IMAGE_SIZE = (110, 50)
CAPTCHA_FONT_SIZE = 30


if DEBUG is False:
    # ========================= CPANEL =========================
    # Database
    # https://docs.djangoproject.com/en/3.2/ref/settings/#databases

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "NAME": "main",
            "USER": "postgres",
            "PASSWORD": "i$3Q2:Sw4-KUx",
            "HOST": "localhost",
            "PORT": "",
        }
    }

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/3.2/howto/static-files/

    STATIC_URL = "/static/"
    MEDIA_URL = "/media/"
    STATICFILES_DIRS = [BASE_DIR / "static"]
    STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"
    STATIC_ROOT = BASE_DIR / "static1"
    MEDIA_ROOT = BASE_DIR / "media"

    # Security
    # CORS_REPLACE_HTTPS_REFERER = True
    # HOST_SCHEME = "https://"
    # SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    # SECURE_SSL_REDIRECT = True
    # SESSION_COOKIE_SECURE = True
    # CSRF_COOKIE_SECURE = True
    # SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    # SECURE_HSTS_PRELOAD = True
    # SECURE_HSTS_SECONDS = 1000000
    # SECURE_FRAME_DENY = True

    # PREPEND_WWW = True

elif DEBUG is True:
    # ========================= LOCAL =========================
    # Database
    # https://docs.djangoproject.com/en/3.2/ref/settings/#databases

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "NAME": "main",
            "USER": "postgres",
            "PASSWORD": "i$3Q2:Sw4-KUx",
            "HOST": "localhost",
            "PORT": "",
        }
    }

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/3.2/howto/static-files/

    STATIC_URL = "/static/"
    MEDIA_URL = "/media/"
    STATICFILES_DIRS = [BASE_DIR / "static"]
    STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
    STATIC_ROOT = BASE_DIR / "static1"
    MEDIA_ROOT = BASE_DIR / "media"

    # Security
    # CORS_REPLACE_HTTPS_REFERER = False
    # HOST_SCHEME = "http://"
    # SECURE_PROXY_SSL_HEADER = None
    # SECURE_SSL_REDIRECT = False
    # SESSION_COOKIE_SECURE = False
    # CSRF_COOKIE_SECURE = False
    # SECURE_HSTS_SECONDS = None
    # SECURE_HSTS_PRELOAD = True
    # SECURE_HSTS_INCLUDE_SUBDOMAINS = False
    # SECURE_FRAME_DENY = False

    # PREPEND_WWW = False
