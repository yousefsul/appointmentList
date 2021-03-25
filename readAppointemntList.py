import logging

import numpy as np
import pandas as pd
from appointmentInfo import AppointmentInfo
from connectMongoDB import ConnectMongoDB

"""
class ReadAppointemntList

Methods:

constructor  --> 
    @:param  appointments list file 

    call from --> main method 
----------------------------------------------------------
get_appointment_list
    @:param no params

    call from --> main method 
----------------------------------------------------------
"""


class ReadAppointemntList:
    """
    * initialize excel file using self reference to the instance
    * replacing not a number fields in the excel sheet with empty string
    * define object from class Appointment as none named appointment_info
    * define appointment as none
    * define object from class ConntecMongoDB named connection
    """

    def __init__(self, appointment_list_file):
        self.appointment_list_file = appointment_list_file
        self.appointment_list_file_dataframe = pd.read_excel(self.appointment_list_file).replace(np.nan, '', regex=True)
        self.appointment_info = None
        self.appointment = None
        self.connection = ConnectMongoDB()

    """
    * read the appointment excel sheet extract the appointment infomartion using the object appointment_info
    """
    def get_appointment_list(self):
        self.connection.connect_to_appointments_collection()
        try:
            for count, row in self.appointment_list_file_dataframe.iloc[::-1].iterrows():
                appointment_data = self.appointment_list_file_dataframe.loc[count]
                self.appointment_info = AppointmentInfo(appointment_data)
                self.appointment = {
                    "date_of_service": self.appointment_info.get_patient_date_of_service(),
                    "place_of_service": self.appointment_info.get_place_of_service(),
                    "patient_name": {
                        "last": self.appointment_info.get_patient_last_name(),
                        "first": self.appointment_info.get_patient_frist_name(),
                        "middle": self.appointment_info.get_patient_middle_name()
                    },
                    "clinician_name": {
                        "last": self.appointment_info.get_clinician_last_name(),
                        "first": self.appointment_info.get_clinician_first_name(),
                    },
                    "modifiers": {
                        "mod1": self.appointment_info.get_modifiers_mod1(),
                        "mod2": self.appointment_info.get_modifiers_mod2(),
                        "mod3": self.appointment_info.get_modifiers_mod3(),
                        "mod4": self.appointment_info.get_modifiers_mod4(),
                    },
                    "billing_code": self.appointment_info.get_patient_billing_code(),
                    "rate_per_unit": self.appointment_info.get_patient_rating(),
                    "units": self.appointment_info.get_patient_unit(),
                    "total_fee": self.appointment_info.get_patient_total_fee(),
                }
                self.connection.insert_to_appointments_collection(self.appointment)
        except ValueError:
            logging.error("get_appointment_list Method      Value Error")
            print("Error from get_appointment_list method", ValueError)
