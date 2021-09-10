import glob
import logging
import shutil
from pathlib import Path

from readAppointemntList import ReadAppointemntList

# formatting my code logging
logging_format = "%(asctime)s =>  %(message)s"
logging.basicConfig(filename="appintmentList.log", filemode="w", format=logging_format, level=logging.INFO,
                    datefmt="%H:%M:%S")


def get_request_files():
    return glob.glob(pathname='request/*.*')


def move_file(req_file):
    shutil.move(req_file, 'completed')


if __name__ == '__main__':
    """
    Main Method

    create object from class ReadAppointemntList named read_appointment_list ,send the file name as param.
    call method get_get_appointment_list()

    @:exception File Maybe not exist
    """
    Path("request").mkdir(parents=True, exist_ok=True)
    Path("completed").mkdir(parents=True, exist_ok=True)
    try:
        print("Start Working ...")
        request_files = get_request_files()
        for file in request_files:
            logging.info("Main Method:          Open DR_AfrozaAhmed excel sheet to read patients data")
            read_appointment_list = ReadAppointemntList(file)
            read_appointment_list.get_appointment_list()
            move_file(file)
    except FileNotFoundError:
        print("Main Method:", FileNotFoundError)
        logging.error("Main Method:         DR_AfrozaAhmed patient excel file doesn't exist")
