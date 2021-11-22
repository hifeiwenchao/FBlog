"""
Django settings for fblog project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path
import configparser
# Build paths inside the project like this: BASE_DIR / 'subdir'.
from django.contrib import admin

BASE_DIR = Path(__file__).resolve().parent.parent

config_path = os.path.join(BASE_DIR, 'config.ini')
parser = configparser.RawConfigParser()
parser.read(config_path, encoding='utf-8')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-yeo6ev=ly7d)cz46@mssp=^b5w1fqfz3-=$4t(n=)7z&=b7*&t'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = parser.get('BASIC', 'env') == 'dev'

ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = [
	'simpleui',  # 第三方后台主题
	'import_export',  # 后台快捷 导入导出 组件
	'mdeditor',  # 第三方 markdown 插件
	# 'admin_reorder',  # 应用程序和模型的自定义排序组件...(更多:https://github.com/mishbahr/django-modeladmin-reorder)
	'captcha',  # 用户登录验证码
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'blog'
]

MIDDLEWARE = [
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	# 'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
	# 网站gzip压缩中间件
	'django.middleware.gzip.GZipMiddleware',
	# 应用程序和模型的自定义排序组件...((更多:https://github.com/mishbahr/django-modeladmin-reorder))
	'admin_reorder.middleware.ModelAdminReorder',
]

ROOT_URLCONF = 'fblog.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [BASE_DIR / 'templates'],
		'APP_DIRS': True,
		'OPTIONS': {
			'context_processors': [
				'django.template.context_processors.debug',
				'django.template.context_processors.request',
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
				# 上下文处理器
				'blog.context_processors.sidebar',
				'blog.context_processors.website_conf',
				# templates中使用 {{ MEDIA_URL }}{{ 文件名 }} 拼接文件地址
				'django.template.context_processors.media',
			],
			# 用于在模板中自动调用静态文件，不需要每个页面使用 {% load static %} 加载静态文件
			'builtins': [
				'django.templatetags.static',
			],
		},
	},
]

WSGI_APPLICATION = 'fblog.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'fblog',
		'USER': parser.get('DB', 'user'),
		'PASSWORD': parser.get('DB', 'password'),
		'HOST': parser.get('DB', 'host'),
		'PORT': parser.get('DB', 'port'),
		'OPTIONS': {'charset': 'utf8mb4'}  # 字符集设置utf8mb4
	}
}

REDIS_HOST = parser.get('REDIS', 'host')
REDIS_PORT = parser.get('REDIS', 'port')
REDIS_AUTH = parser.get('REDIS', 'password')

# redis 默认配置
CACHES = {
	"default": {
		"BACKEND": "django_redis.cache.RedisCache",
		"LOCATION": f'redis://:{REDIS_AUTH}@{REDIS_HOST}:{REDIS_PORT}/1',
		"OPTIONS": {
			"IGNORE_EXCEPTIONS": True,  # memcached 异常行为
			"CONNECTION_POOL_KWARGS": {"max_connections": 100},  # 配置默认连接池
			"PICKLE_VERSION": -3,
			"CLIENT_CLASS": "django_redis.client.DefaultClient",
		},
	}
}

REDIS_TIMEOUT = 7 * 24 * 60 * 60
CUBES_REDIS_TIMEOUT = 60 * 60
NEVER_REDIS_TIMEOUT = 365 * 24 * 60 * 60

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators
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
# https://docs.djangoproject.com/en/3.2/topics/i18n/
LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
STATIC_URL = '/static/'
# 当你关闭DEBUG模式时，需要打开STATIC_ROOT注释，同时注释掉STATICFILES_DIRS，然后执行命令收集静态文件：python manage.py collectstatic
# STATIC_ROOT = BASE_DIR / 'static'
STATICFILES_DIRS = (
	BASE_DIR / 'static',
)

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'static/media'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

"""
后台models自定义排序：(两个库都还有其他用法，请自行查看官方文档)
1，admin_reorder 第三方库
2，simpleui 第三方库集成

使用说明：
如果您使用 admin_reorder 排序，需注释掉 SIMPLEUI_CONFIG 字段并打开app: admin_reorder的注释
如果您使用 simpleui 排序，需要注释掉app: admin_reorder
两者只能使用其一，使用哪一个就注释掉另一个
"""
# admin_reorder 排序后台app导航栏
ADMIN_REORDER = (
	# Reorder app models
	{'app': 'blog', 'models': (
		'blog.SiteUser'
		'blog.Carousel',
		'blog.Announcement',
		'blog.Conf',
		'blog.Article',
		'blog.ArticleImg',
		'blog.Subscription',
		'blog.Category',
		'blog.Tag',
		'blog.Comment',
		'blog.Pay',
		'blog.Friend',
		'blog.About'
	)},
)

# simpleui 排序后台app导航栏
SIMPLEUI_CONFIG = {
	'system_keep': True,
	'menu_display': ['内容管理', '配置管理', '订阅管理', '用户管理', ],
	'dynamic': True,
	'menus': [{
		'name': '内容管理',
		'models': [{
			'name': '文章banner',
			'url': '/admin/blog/articleimg'
		}, {
			'name': '文章列表',
			'url': '/admin/blog/article'
		}, {
			'name': '文章分类',
			'icon': 'fa fa-list',
			'url': '/admin/blog/category'
		}, {
			'name': '文章标签',
			'icon': 'fa fa-tags',
			'url': '/admin/blog/tag'
		}, {
			'name': '评论列表',
			'icon': 'fa fa-comments',
			'url': '/admin/blog/comment'
		}]
	}, {
		'name': '配置管理',
		'models': [{
			'name': '基础配置',
			'url': '/admin/blog/conf'
		}, {
			'name': '首页轮播图',
			'url': '/admin/blog/carousel'
		}, {
			'name': '网站公告',
			'icon': 'fas fa-bullhorn',
			'url': '/admin/blog/announcement'
		}, {
			'name': '友链',
			'icon': 'fa fa-link',
			'url': '/admin/blog/friend'
		}, {
			'name': '收款图',
			'icon': 'fa fa-coffee',
			'url': '/admin/blog/pay'
		}, {
			'name': "关于",
			'icon': 'fa fa-id-card',
			'url': '/admin/blog/about'
		}]
	}, {
		'name': '订阅管理',
		'models': [{
			'name': '订阅列表',
			'url': '/admin/blog/subscription'
		}]
	}, {
		'name': '用户管理',
		'icon': 'fas fa-user-shield',
		'models': [{
			'name': '用户',
			'icon': 'fa fa-user',
			'url': 'auth/user/'
		}, {
			'name': '用户组',
			'icon': 'fa fa-users',
			'url': 'auth/group/'
		}, {
			'name': '网站用户',
			'icon': 'fa fa-users',
			'url': '/admin/blog/siteuser'
		}, ]
	}]
}

# simpleui本地配置
# SIMPLEUI_LOGO：对官方css进行了某些修改以适应后台尺寸，使用个人logo时根据显示情况自行修改即可...
SIMPLEUI_LOGO = '/static/images/logo/logo.png'
SIMPLEUI_HOME_TITLE = 'FBlog后台管理'
SIMPLEUI_ANALYSIS = False
SIMPLEUI_LOADING = False
SIMPLEUI_DEFAULT_ICON = True
SIMPLEUI_HOME_INFO = False

# 后台header, title
admin.AdminSite.site_header = SIMPLEUI_HOME_TITLE
admin.AdminSite.site_title = SIMPLEUI_HOME_TITLE

# 登录后重定向到/blog/页面
LOGIN_REDIRECT_URL = '/blog/'

# session设置
SESSION_COOKIE_AGE = 86400*7  # Session的cookie失效日期（秒）
SESSION_EXPIRE_AT_BROWSER_CLOSE = True  # 是否关闭浏览器使得Session过期

# 字母验证码
CAPTCHA_IMAGE_SIZE = (100, 36)  # 设置 captcha 图片大小
CAPTCHA_LENGTH = 4  # 字符个数
CAPTCHA_TIMEOUT = 3  # 超时(minutes)

# SMTP服务器
# 请更改为自己的邮箱配置
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = parser.get('SMTP', 'host')
EMAIL_HOST_USER = parser.get('SMTP', 'user')
# 密码(请替换为你自己的哟) qq为设置=>账户=>POP3/IMAP/SMTP/Exchange/CardDAV/CalDAV服务=> 开启服务POP3/SMTP服务=> 生成授权码
EMAIL_HOST_PASSWORD = parser.get('SMTP', 'password')
# 发送邮件端口和加密（两种方式不能同时使用）
# 云服务器使用：
EMAIL_PORT = parser.get('SMTP', 'port')
EMAIL_USE_SSL = parser.get('SMTP', 'use_ssl')
# 默认的发件人
DEFAULT_FROM_EMAIL = 'feiwenchao'
