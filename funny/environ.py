#coding=utf-8
import sys, os
from funny import funny

# 加入需要import的路径
ROOT = os.path.join(os.path.dirname(os.path.realpath(__file__)), './')
CONTROLLER = os.path.join(ROOT, 'controller')
VIEW = os.path.join(ROOT, 'view')
TOOLS = os.path.join(ROOT, 'tools')

sys.path.insert(0, ROOT)
sys.path.insert(0, CONTROLLER)
sys.path.insert(0, VIEW)
sys.path.insert(0, TOOLS)

import logging
import logging.config

CONF_LOG = "log_config"
logging.config.fileConfig(CONF_LOG);

# set the secret key.  keep this really secret:
funny.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT2'

# login相关
from flask.ext.login import current_user
from flask.globals import g
@funny.before_request
def before_request():
    g.user = current_user

from flask.ext.login import LoginManager
login_manager = LoginManager()
login_manager.init_app(funny)
