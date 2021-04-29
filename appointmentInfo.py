import datetime

from bson import Decimal128

"""
class Appointment

Methods:

constructor  -->
    param : appointment info

    call from --> get_appointment_list method in ReadAppointemntList class
----------------------------------------------------------
getters
----------------------------------------------------------
"""


class AppointmentInfo:
    """
    read the appointment info
    get the paitent name
    get the clinician name
    get the date and time for the appointment
    """
    def __init__(self, appointment_info):
        self.appointment_info = appointment_info
        self.patient_name = self.appointment_info.get("Client")
        self.patient_full_name = self.patient_name.split()
        self.middle_name = ""
        self.clinician_full_name = self.appointment_info.get("Clinician").split(" ")
        self.date_and_time = ""
        self.date = ""
        self.date_of_service = ""

    def get_patient_frist_name(self):
        return self.patient_full_name[0]

    def get_patient_last_name(self):
        if len(self.patient_full_name) == 2:
            return self.patient_full_name[1]
        else:
            self.middle_name = self.patient_full_name[1]
            return self.patient_full_name[2]

    def get_patient_middle_name(self):
        return self.middle_name

    def get_clinician_first_name(self):
        return self.clinician_full_name[0]

    def get_clinician_last_name(self):
        return self.clinician_full_name[1]

    def get_patient_billing_code(self):
        return str(self.appointment_info.get("Billing Code"))

    def get_patient_unit(self):
        return int(self.appointment_info.get("Units"))

    def get_patient_rating(self):
        rating = Decimal128(str(self.appointment_info.get("Rate per Unit")))
        patient_rating = "{:.2f}".format(rating.to_decimal())
        return Decimal128(patient_rating)

    def get_patient_total_fee(self):
        total = Decimal128(str(self.appointment_info.get("Total Fee")))
        total_fee = "{:.2f}".format(total.to_decimal())
        return Decimal128(total_fee)

    def get_patient_date_of_service(self):
        self.date_and_time = self.appointment_info.get("Date of Service").split(" ")
        self.date = self.date_and_time[0].split("/")
        self.date_of_service = self.date[2] + self.date[0] + self.date[1]
        return self.date_of_service

    def get_patient_charge(self):
        return Decimal128(str(self.appointment_info.get("Charge")))

    def get_patient_uninvoiced(self):
        return Decimal128(str(self.appointment_info.get("Uninvoiced")))

    def get_patient_paid(self):
        return Decimal128(str(self.appointment_info.get("Paid")))

    def get_patient_unpaid(self):
        return Decimal128(str(self.appointment_info.get("Unpaid")))

    def get_patient_check_number(self):
        return self.appointment_info.get("Check Number")

    def get_patient_payment_status(self):
        return self.appointment_info.get("Client Payment Status")

    def get_place_of_service(self):
        return "0" + str(self.appointment_info.get("POS"))

    def get_modifiers_mod1(self):
        return str(self.appointment_info.get("Modifier1"))

    def get_modifiers_mod2(self):
        return self.appointment_info.get("Modifier2")

    def get_modifiers_mod3(self):
        return self.appointment_info.get("Modifier3")

    def get_modifiers_mod4(self):
        return self.appointment_info.get("Modifier4")


    def get_current_status(self):
        current_status = {
            "status": "new",
            "date": {
                "date": datetime.datetime.now().date().strftime("%Y%m%d"),
                "time": datetime.datetime.now().time().strftime("%H:%M:%S")
            }
        }
        return current_status