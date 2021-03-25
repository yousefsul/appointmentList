import logging
from readAppointemntList import ReadAppointemntList

# formatting my code logging
logging_format = "%(asctime)s =>  %(message)s"
logging.basicConfig(filename="appintmentList.log", filemode="w", format=logging_format, level=logging.INFO,
                    datefmt="%H:%M:%S")

# ? add paitnets file name 
EXCEL_FILE_NAME_APPOINTMENTS_LIST = "Appointments_Report_03.03_to_03.06.2021.xlsx"

if __name__ == '__main__':
    """
    * Main Method

    * create object from class ReadAppointemntList named read_appointment_list ,send the file name as param.
    * call method get_get_appointment_list()

    @:exception File Maybe not exist
    """
    try:
        logging.info("Main Method:          Open DR_AfrozaAhmed excel sheet to read patients data")
        read_appointment_list = ReadAppointemntList(EXCEL_FILE_NAME_APPOINTMENTS_LIST)
        read_appointment_list.get_appointment_list()
    except FileNotFoundError:
        print("Main Method:", FileNotFoundError)
        logging.error("Main Method:         DR_AfrozaAhmed patient excel file doesn't exist")