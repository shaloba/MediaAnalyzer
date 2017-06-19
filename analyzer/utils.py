import subprocess
import csv
import os
import logging
import config


def execute_process(command):
    """
    Executing new process
    :param command: execution command
    :return: boolean, True in case the process succeeded, otherwise False
    """
    success = True
    exit_code = subprocess.call(command, shell=True)
    if exit_code != 0:
        success = False

    return success


def file_generator(file_object):
    """
    Uses a generator to read a large file lazily
    :param file_object: file instance
    :return: file line
    """
    while True:
        data = file_object.readline()
        if not data:
            break
        yield data.split(config.CSV_DELIMITER)


def process_frames_csv_file(src_file, csv_outut):
    """
    Read csv file using generator, extract certain fields and contain them into onother csv file.
    :param src_file: the origin csv file path
    :param csv_outut: the new csv file path
    :return: boolean value, True in case of successful processing, otherwise False
    """
    frame_idx = 0
    csv_headers = ['frame_index', 'frame_size']
    if csv_outut is None:
        csv_writer = None
    else:
        csv_output_path = os.path.join(config.OUTPUT_DIR_PATH, csv_outut)
        frames_csv = open(csv_output_path, 'w')
        csv_writer = csv.writer(frames_csv, delimiter=config.CSV_DELIMITER)
        csv_writer.writerow(csv_headers)

    statistic_data = dict(sizes_sum=0,
                          frames_count=0,
                          smallest_frame=0,
                          biggest_frame=0,
                          frames_avg=0)
    try:
        with open(src_file) as file_handler:
            file_gen = file_generator(file_handler)
            for line in file_gen:
                frame_size = int(line[1].strip())
                if csv_writer:
                    csv_writer.writerow([frame_idx, frame_size])


                if frame_idx == 0:
                    statistic_data['smallest_frame'] = frame_size

                if frame_size < statistic_data['smallest_frame']:
                    statistic_data['smallest_frame'] = frame_size

                if frame_size > statistic_data['biggest_frame']:
                    statistic_data['biggest_frame'] = frame_size
                statistic_data['sizes_sum'] += frame_size
                frame_idx += 1

            statistic_data['frames_count'] = frame_idx
            statistic_data['frames_avg'] = statistic_data['sizes_sum'] / frame_idx


    except Exception as err:
        statistic_data = None
        logging.error('Error occurred [src file]: %s [err]: %s' % (src_file, str(err)))

    return statistic_data


def print_stats(stats_obj):
    """
    Print the frames statistic data
    :param stats_obj: dictionary contains the statistic data
    :return:
    """
    print "#" *30
    for key, value in stats_obj.iteritems():
        if config.STATS_MSG.get(key):
            print config.STATS_MSG[key] % value

    print "#" * 30