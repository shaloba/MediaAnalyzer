import requests
import os
import settings
import logging

def download_file(url):
    """
    Download file to the file system
    :param url: file url
    :return: downloaded file path in case of success, otherwise None
    """
    download_path = None
    try:
        tmp_sample_name = url.split('/')[-1]
        download_path = os.path.join(settings.output_path, tmp_sample_name)
        r = requests.get(url, stream=True)
        with open(download_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)
    except Exception as err:
        logging.error('Error occur while downloading the file [url]: %s [err]: %s' % (url, str(err)))

    return download_path


def delete_file(file_path):
    """
    Delete file from the file system
    :param file_path: the file location
    :return:
    """
    try:
        os.remove(file_path)
    except Exception as err:
        logging.error('Failed to remove file [file path]: %s [err]: %s' % (file_path, str(err)))

