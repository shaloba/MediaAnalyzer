__author__ = "Shlomy Balulu"


from argparse import ArgumentParser
import sys
import logging

class ArgsParser():

    def __init__(self):
        self.__args = self.parse()

    def parse(self):
        """
        extracting user input using python argparse lib
        :return: args object (ArgumentParser instance)
        """
        try:
            parser = ArgumentParser()
            parser.add_argument('--input', help="specify the media file location")
            parser.add_argument('--csv_frames_report', help="specify the csv frame file name")
            args = parser.parse_args()
        except Exception as err:
            logging.error(err)
            return None

        return args

    def get_args(self):
        if self.__args.input is None:
            print 'Arguments Error:\nPlease specify the media file path\n\naborting.'
            sys.exit(1)
        return self.__args.__dict__
