import os
import logging


# application port
PORT = 8001

# application host
HOST = '0.0.0.0'
output_path = '/tmp/ffprobe'
log_dir = '/var/log/ffprobe'
log_name = 'web_service.log'


if os.path.isdir(output_path) is False:
    os.mkdir(output_path)

