SECRET_KEY = '781e0!t+BOOGERSgwkgpw-+e^6^vhvphr=_*=*jCHEESE6z7v-d@d#cawckv2++'

ALLOWED_HOSTS = ['167.99.229.37', 'jeremiahjthompson.com', 'www.jeremiahjthompson.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'portfoliodb',
        'USER': 'djangodbman',
        'PASSWORD': 'password1234',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

DEBUG = False
