import os
import logging
import settings

if os.path.isdir(settings.log_dir) is False:
    os.mkdir(settings.log_dir)


logging.basicConfig(filename=os.path.join(settings.log_dir, settings.log_name), level=logging.DEBUG)