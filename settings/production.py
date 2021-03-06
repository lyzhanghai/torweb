# coding:utf-8

from settings.common import *


# BACKEND_MONGO = "mongodb://127.0.0.1/torweb"
# BACKEND_REDIS = ('localhost', 6379, 0)

# MySQL Database
BACKEND_MYSQL = {
    'database': 'torweb',
    'max_connections': 20,
    'stale_timeout': 300,
    'user': 'root',
    'password': 'qwaszx',
    'host': '127.0.0.1',
    'port': 3306
}
# Static Path
STATIC_PATH = (
    (r'/static/(.*)', {'path': 'frontend/templates/static/'}),
    (r'/assets/(.*)', {'path': 'frontend/static/assets/'}),
    (r'/blog/assets/(.*)', {'path': 'docs/assets/'}),
    (r'/dashboard/(.*)', {'path': 'frontend/templates/dashboard/'})
)