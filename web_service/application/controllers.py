__author__ = 'shaloba'
from flask import request
from application import app, utils
from analyzer import analayze_frames_sizes
import json
import os

@app.route('/info/frames', methods=['GET'])
def frames_info():
    """
    Retrieve a media file frames statistic data
    :param: input- the media file path
    :return: json contains the statistic data
    """
    response = {'success': True}
    data = request.args
    stats = None
    if data.get('input'):
        file_input = data['input']
        if file_input.startswith('file'):
            file_path = file_input.replace('file://', '')
            if(os.path.isfile(file_path)) is True:
                stats = analayze_frames_sizes.get_frames_data(file_path, None)

            else:
                response['success'] = False
                response['err_msg'] = "File does not exist"
        elif file_input.startswith('http'):
            file_path = utils.download_file(file_input)
            if file_path:
                stats = analayze_frames_sizes.get_frames_data(file_path, None)
                utils.delete_file(file_path)# delete the downloaded file

        else:
            response['success'] = False
            response['err_msg'] = "Invalid Parameters"

        if stats is None:
            response['success'] = False
            response['err_msg'] = "Failed to process the requested file"
        else:
            response['stats'] = stats
    else:
        response['err_msg'] = 'Invalid Parameters'

    return json.dumps(response)
