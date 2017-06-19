import os
import logging

LOG_DIR = '/var/log/ffprobe'
LOG_name = 'ffprobe_analyzer.log'

logging.basicConfig(filename=os.path.join(LOG_DIR, LOG_name), level=logging.DEBUG)

FRAMES_FILE_NAME = 'frames.csv'
CSV_DELIMITER = ','
OUTPUT_DIR_NAME = 'output'
OUTPUT_DIR_PATH = '/tmp/ffprobe'
STATS_MSG = dict(sizes_sum="Total frames size: %s",
                      frames_count="Total frames count: %s",
                      smallest_frame="Smallest frame size: %s",
                      biggest_frame="Biggest frame size: %s",
                      frames_avg="Frames average size: %s")