__author__ = 'shaloba'


import os
from args_parser import ArgsParser
import utils
import config
import logging


def get_frames_data(file_path, csv_output):
    """
    Retrieve video and audio files frame data
    :param file_path: file full path
    :param csv_output: csv output file name
    :return:
    """
    stats = None
    ffprobe_frames_out = os.path.join(config.OUTPUT_DIR_PATH, config.FRAMES_FILE_NAME)
    cmd = 'ffprobe -show_frames -select_streams v -show_entries frame=pkt_size -print_format csv %s 1> %s 2>/dev/null' % (file_path, ffprobe_frames_out)
    success_flag = utils.execute_process(cmd)
    if success_flag is True:
        stats = utils.process_frames_csv_file(ffprobe_frames_out, csv_output)
        if stats is not None:
            utils.print_stats(stats)
    else:
        logging.error('Error processing %s data' % file_path)

    if os.path.isfile(ffprobe_frames_out):
        os.remove(ffprobe_frames_out)

    return stats

if __name__ == '__main__':
    arg_parser = ArgsParser()
    args = arg_parser.get_args()
    get_frames_data(args['input'], args['csv_frames_report'])