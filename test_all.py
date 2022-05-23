"""
This Test module for Hospital management system.

Writen by Donggyu Kim

This module includes a lot of test classes.
Because it is not a library to use other modules, there is no type hinting.
"""

from datetime import timedelta

import pytest
from freezegun import freeze_time

from main import (
    PersonType,
    DoctorType,
    DateType,
    PatientType,
    ChargeHistoryItem,
    BillType,
)


class TestEncapsulation:
    """
    This class test encapsulation.
    - When you try to set a value, it works normally without any Exception.
    - When you try to set a value to readonly property, it raises an Exception.
    """

    # Test cases
    person = PersonType('F', 'L')
    doctor = DoctorType('F', 'L', 'S')
    patient = PatientType('F', 'L', 32, DateType(2011, 1, 1), doctor, DateType(2022, 4, 13))
    charge_history_item = ChargeHistoryItem(32, 'medicine')
    bill = BillType(patient)

    # Test for PersonType
    def test_person_set_first_name(self):
        self.person.first_name = 'f'

    def test_person_set_last_name(self):
        self.person.last_name = 'l'

    # Test for DoctorType
    def test_doctor_set_speciality(self):
        self.doctor.speciality = 's'

    # Test for PatientType
    def test_patient_try_to_set_id(self):
        # If setter is not defined, AttributeError is raised.
        with pytest.raises(AttributeError):
            self.patient.id = 1

    def test_patient_set_age(self):
        self.patient.age = 1

    def test_patient_try_to_set_birthday(self):
        # If setter is not defined, AttributeError is raised.
        with pytest.raises(AttributeError):
            self.patient.birthday = DateType(2011, 2, 2)

    def test_patient_set_attending_physician(self):
        self.patient.attending_physician = DoctorType('FF', 'LL', 'SS')

    def test_patient_try_to_set_admitted_date(self):
        # If setter is not defined, AttributeError is raised.
        with pytest.raises(AttributeError):
            self.patient.admitted_date = DateType(2011, 2, 2)

    def test_patient_set_discharged_date(self):
        self.patient.discharged_date = DateType(2022, 4, 15)

    # Test for ChargeHistoryItem
    def test_charge_history_item_try_to_set_cost(self):
        # If setter is not defined, AttributeError is raised.
        with pytest.raises(AttributeError):
            self.charge_history_item.cost = 1

    def test_charge_history_item_set_category(self):
        self.charge_history_item.category = 'medicine'

    def test_charge_history_item_set_description(self):
        self.charge_history_item.description = '1'

    # Test for BillType
    def test_bill_try_to_set_patient(self):
        # If setter is not defined, AttributeError is raised.
        with pytest.raises(AttributeError):
            self.bill.patient = self.patient


class TestPropertyValidation:
    """
    This class test validation routine.
    - If an incorrect value is entered, is the correct exception raised or not.
    """

    # Test Cases
    person = PersonType('F', 'L')
    doctor = DoctorType('F', 'L', 'S')
    patient = PatientType('F', 'L', 32, DateType(2011, 1, 1), doctor, DateType(2022, 4, 13))
    charge_history_item = ChargeHistoryItem(32, 'medicine')
    bill = BillType(patient)

    # test for PersonType
    def test_person_set_first_name_if_not_str(self):
        # when you try to set int,
        # TypeError will be raised.
        with pytest.raises(TypeError):
            self.person.first_name = 1

    def test_person_set_first_name_if_not_alphabet(self):
        # when you try to set non alphabet str,
        # ValueError will be raised.
        with pytest.raises(ValueError):
            self.person.first_name = '1'

    def test_person_set_last_name_if_not_str(self):
        # when you try to set int,
        # TypeError will be raised.
        with pytest.raises(TypeError):
            self.person.last_name = 1

    def test_person_set_last_name_if_not_alphabet(self):
        # when you try to set non alphabet str,
        # ValueError will be raised.
        with pytest.raises(ValueError):
            self.person.last_name = '1'

    # test for DoctorType
    def test_doctor_set_speciality_if_not_str(self):
        # when you try to set int,
        # TypeError will be raised.
        with pytest.raises(TypeError):
            self.doctor.speciality = 1

    def test_doctor_set_speciality_if_not_alphabet(self):
        # when you try to set non alphabet str,
        # ValueError will be raised.
        with pytest.raises(ValueError):
            self.doctor.speciality = '1'

    # test for PatientType
    def test_patient_set_age_if_not_int(self):
        # when you try to set str,
        # TypeError will be raised.
        with pytest.raises(TypeError):
            self.patient.age = '10'

    def test_patient_set_attending_physician_if_not_doctor(self):
        # when you try to set DoctorType,
        # TypeError will be raised.
        with pytest.raises(TypeError):
            self.patient.attending_physician = self.person

    def test_patient_set_discharged_date_if_not_date(self):
        # when you try to set date,
        # TypeError will be raised.
        with pytest.raises(TypeError):
            self.patient.discharged_date = None

    def test_patient_set_discharged_date_if_it_is_same_date(self):
        # when you try to set same date or past date,
        # ValueError will be raised.
        with pytest.raises(ValueError):
            self.patient.discharged_date = DateType(2022, 4, 13)  # same date

    # test for ChargeHistoryItem
    def test_charge_history_item_create_new_object_if_it_is_wrong_category(self):
        # when you try to set wrong category which is not in categories,
        # ValueError will be raised.
        with pytest.raises(ValueError):
            ChargeHistoryItem(
                321,
                '1'  # wrong category
            )

    def test_charge_history_item_add_new_category_if_not_str(self):
        # when you try to add a new category, if the value is not str,
        # TypeError will be raised.
        with pytest.raises(TypeError):
            ChargeHistoryItem.add_new_category(123)

    def test_charge_history_item_add_new_category_if_not_alphabet(self):
        # when you try to add a new category, if the value does not consist of only alphabet,
        # ValueError will be raised.
        with pytest.raises(ValueError):
            ChargeHistoryItem.add_new_category('123')

    def test_charge_history_item_change_category_if_not_str(self):
        # when you try to set category of an instance, but if the value is not str
        # TypeError will be raised.
        with pytest.raises(TypeError):
            self.charge_history_item.category = 1

    def test_charge_history_item_change_category_if_not_alphabet(self):
        # when you try to set category of an instance,
        # but although the value is str, if it does not consist of only alphabet,
        # ValueError will be raised.
        with pytest.raises(ValueError):
            self.charge_history_item.category = '1'

    def test_bill_getitem_if_not_slice_or_int(self):
        # create test case
        self.bill.add_charge(231, 'medicine')

        # when you try to get some item using str like dict,
        # TypeError will be raised.
        with pytest.raises(TypeError):
            self.bill['0']


class TestPatientMethod:
    """
    This class test PatientType's Methods.
    - When try to use the method, is it work like what I designed.
    """

    # test case
    doctor = DoctorType('F', 'L', 'S')
    patient = PatientType('F', 'L', 32, DateType(2011, 1, 1), doctor, DateType(2022, 4, 13))

    def test_patient_get_duration_if_discharged_date_is_none(self):
        # is the duration property returns correct type or not
        # it must be timedelta.
        assert isinstance(self.patient.duration, timedelta)

    @freeze_time('2022-04-22')  # set specific date
    def test_patient_update_discharged_date_as_today(self):
        # when you try to update discharged_date, is it same with today's date
        self.patient.update_discharged_date_as_today()

        # compare with sample str using strftime method.
        assert '2022-04-22' == self.patient.discharged_date.strftime('%Y-%m-%d')


class TestChargeHistoryItemMethod:
    """
    This class test ChargeHistoryItem's Methods.
    - When try to use the method, is it work like what I designed.
    """

    # test case
    charge_history_item = ChargeHistoryItem(32, 'medicine')

    def test_charge_history_item_add_new_category(self):
        # when you add a new category, is it appended in categories?
        self.charge_history_item.add_new_category('aaa')

        # if not, the express will be False
        assert 'aaa' in self.charge_history_item.categories

    def test_charge_history_item_add_operator_with_same_instance(self):
        # when try to use add operation with other instance,
        # is it return correct value and correct type?
        assert isinstance(self.charge_history_item + self.charge_history_item, int)

    def test_charge_history_item_add_operator_with_int(self):
        # when try to use add operation with int type,
        # is it work or not?

        # if it works, it returns int type.
        assert isinstance(self.charge_history_item + 2, int)


class TestBillMethod:
    """
    This class test BillType's Methods.
    - When try to use the method, is it work like what I designed.
    """

    # test cases
    doctor = DoctorType('F', 'L', 'S')
    patient = PatientType('F', 'L', 32, DateType(2011, 1, 1), doctor, DateType(2022, 4, 13))
    bill = BillType(patient)

    def test_bill_add_new_charge_history_item(self):
        # add new ChargeHistoryItem for comparing.
        new_item = ChargeHistoryItem(233, 'medicine')

        # add_charge in bill
        self.bill.add_charge(new_item.cost, new_item.category)

        # compare sample item.
        assert str(new_item) == str(self.bill[0])

    def test_bill_remove_an_charge_history_item(self):
        # try to remove some item
        self.bill.remove_charge(0)

        # if it works, __charge_history's length is 0
        assert len(self.bill) == 0


class TestCastingStr:
    """
    This class test __str__() of whole classes.
    - When try to call str({class_name}), if it works, there is not any Exception.
    """

    # test cases
    person = PersonType('F', 'L')
    doctor = DoctorType('F', 'L', 'S')
    patient = PatientType('F', 'L', 32, DateType(2011, 1, 1), doctor, DateType(2022, 4, 13))
    charge_history_item = ChargeHistoryItem(32, 'medicine')
    bill = BillType(patient)

    def test_person_str(self):
        str(self.person)

    def test_doctor_str(self):
        str(self.doctor)

    def test_patient_str(self):
        str(self.patient)

    def test_charge_history_item_str(self):
        str(self.charge_history_item)

    def test_bill_str(self):
        # to test, we need to add new charge_history_item
        self.bill.add_charge(
            self.charge_history_item.cost,
            self.charge_history_item.category
        )
        str(self.bill)


class TestLinkage:
    """
    This class test linkage with reference attributes like Attending Physician.
    - When try to get some data using reference attribute, is it works or not?
    """

    # test cases
    doctor = DoctorType('S', 'F', 'L')
    patient = PatientType('F', 'L', 32, DateType(2011, 1, 1), doctor, DateType(2022, 4, 13))
    bill = BillType(patient)

    def test_patient_get_doctor_last_name(self):
        # if it works, it will return 'L'
        assert 'L' == self.patient.attending_physician.last_name

    def test_bill_get_patient_first_name(self):
        # if it works, it will return 'F'
        assert 'F' == self.bill.patient.first_name

    def test_bill_get_doctor_speciality(self):
        # if it works, it will return 'S'
        assert 'S' == self.bill.patient.attending_physician.speciality


class TestUseCases:
    """
    This is Scenario-Based test.
    It is similar with real case.
    """

    # doctors
    doctor_lee = DoctorType('Xiao Lang', 'Lee', 'Internal Medicine')
    doctor_edison = DoctorType('Thomas', 'Edison', 'General Surgery')

    # list for management objects.
    patients = []
    bills = []

    @freeze_time('2022-04-14')
    def test_new_patients_admitted(self):
        """
        14/04/2022 two new patient come to hospital.

        One patient got doctor Lee.
        Another patient got doctor Edison.

        They came same date.
        """

        # first patient added
        self.patients.append(
            PatientType(
                'Chis',
                'A',
                18,
                DateType(2011, 3, 13),
                self.doctor_lee,
                DateType.today(),
            )
        )

        # second patient added
        self.patients.append(
            PatientType(
                'Sasara',
                'Satou',
                21,
                DateType(2010, 4, 1),
                self.doctor_edison,
                DateType.today(),
            )
        )

        # validate data
        assert len(self.patients) == 2
        assert self.patients[0].first_name == 'Chis'
        assert self.patients[1].attending_physician == self.doctor_edison

    def test_second_patient_last_name_is_changed(self):
        """
        Independent case: when the patient's last name is changed.

        2nd Patient: Satou -> Sato
        """
        self.patients[1].last_name = 'Sato'

        assert self.patients[1].last_name == 'Sato'

    def test_aging_all_patients(self):
        """
        Independent case: when whole patient are aging.

        1st Patient: 18 -> 19
        2nd Patient: 21 -> 22
        """

        for patient in self.patients:
            patient.age += 1

        assert self.patients[0].age == 19
        assert self.patients[1].age == 22

    def test_change_attending_physician_of_first_patient(self):
        """
        Independent case: when attending physician is changed

        1st Patient: doctor_lee -> doctor_edison
        """
        self.patients[0].attending_physician = self.doctor_edison

        assert self.patients[0].attending_physician == self.doctor_edison

    def test_billing_for_medicine_and_meeting_doctor(self):
        """
        Meet doctor and take a new medicine
        """

        # create new bills
        self.bills.append(BillType(self.patients[0]))
        self.bills.append(BillType(self.patients[1]))

        # add 1st patient's bill history.
        self.bills[0].add_charge(20, 'doctor')
        self.bills[0].add_charge(42, 'medicine')
        self.bills[0].add_charge(20, 'doctor')
        self.bills[0].add_charge(20, 'doctor', 'rehabilitation treatment')

        # add 2nd patient's bill history.
        self.bills[1].add_charge(20, 'doctor')
        self.bills[1].add_charge(20, 'doctor', 'wound disinfection')
        self.bills[1].add_charge(42, 'medicine')
        self.bills[1].add_charge(20, 'doctor')

    def test_cancel_wrong_medicine_fee_and_prescribing_a_new_medicine(self):
        """
        2nd patient prescribing wrong medicine before.
        We have to cancel it, and prescribe a new medicine.
        """

        # to cancel, remove that item from bill
        removed = self.bills[1].remove_charge(2)

        # check bill if it works or not
        assert removed.cost == 42
        assert len(self.bills[1]) == 3

        # add correct medicine
        self.bills[1].add_charge(32, 'medicine')

        # check bill if it works or not again
        assert len(self.bills[1]) == 4
        assert self.bills[1][3].cost == 32

    def test_add_treatment_category_and_update_bills(self):
        """
        Independence case: when you need to add new category

        we need to add a new category and update existing items.
        - if the description is not None, it is treatment.
        """

        # add a new category
        ChargeHistoryItem.add_new_category('treatment')

        # update 1st patient's items.
        for i in range(len(self.bills[0])):
            if self.bills[0][i].description is not None:
                self.bills[0][i].category = 'treatment'

        # update 2nd patient's items.
        for i in range(len(self.bills[1])):
            if self.bills[1][i].description is not None:
                self.bills[1][i].category = 'treatment'

        # check sample data
        assert self.bills[0][3].category == 'treatment'
        assert self.bills[1][1].category == 'treatment'

    @freeze_time('2022-04-22')
    def test_discharge_first_patient(self):
        """
        1st patient is discharged.
        We need to update discharged date, and get total fee.
        Also, we need to add room rental fees (day per $22).
        """

        # update discharged date
        self.patients[0].update_discharged_date_as_today()

        # test duration property
        assert self.patients[0].duration.days == 8

        # add room rental fees
        for _ in range(self.patients[0].duration.days):
            self.bills[0].add_charge(22, 'room')

        # get total fee.
        assert self.bills[0].total_fee == 278
