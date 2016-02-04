# -*- coding: utf-8 -*-
#!/usr/bin/env python
from funny import funny
import logging
import logging.config

CONF_LOG = "log_config"
logging.config.fileConfig(CONF_LOG);

funny.run(debug=True,host='0.0.0.0',port=8082)
