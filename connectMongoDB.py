from pymongo import *
import logging

MONGO_CLIENT = "mongodb://yousef:Ys2021xch@209.151.150.58:63327/?authSource=admin&readPreference=primary&appname" \
               "=MongoDB%20Compass&ssl=false"

"""
class ConnectMongoDB

Methods:

constructor  --> 
    no params 

    call from --> get_appointment_list method in ReadExcelSheet class
---------------------------------------------------------------------------------
connect_to_appointments_collection
    no params

    call from --> get_appointment_list method in ReadAppointemntList class
----------------------------------------------------------------------------------
insert_to_appointments_collection
    param result of the patient data 

    call from --> get_appointment_list method in ReadAppointemntList class
----------------------------------------------------------------------------------

"""


class ConnectMongoDB:
    """
    connect to Mongodb
    initalze the database of dr_aforza ahmed
    define the appointments_collection
    """

    def __init__(self):
        try:
            self.mongo_client = MongoClient(MONGO_CLIENT)
            self.db = self.mongo_client.client_2731928905_DB
            self.appointments_collection = None
        except ConnectionError:
            logging.error("constructor Method:         Error while connect to mongoDB")
            print("Error while connection to mongoDB")

    """
    create connection to paitnets collection in dr afroza ahmed db 
    """

    def connect_to_appointments_collection(self):
        self.appointments_collection = self.db.appointmentsColl

    """
    insert the appointment data into mongodb 
    """
    def insert_to_appointments_collection(self, result):
        try:
            self.appointments_collection.insert(result)
            logging.warning("insert_to_appointments_collection Method:         Insert appointment data to appointments "
                            "collection")
        except Exception as e:
            logging.warning("insert_to_appointments_collection Method:         Error While inserting records to "
                            "appointments collection")
            print("An exception have occurred ", e)
