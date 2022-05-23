"""
Hospital management system

Writen by Donggyu Kim

This module includes three classes and two subclasses for inheritance.
"""

from datetime import timedelta
from typing import Union, List, Optional


class PersonType:
    """
    This is base class for DoctorType, PatientType.
    It has first_name and last_name.
    Both attribute is required.
    """

    def __init__(self, first_name: str, last_name: str):
        """
        Initializer for PersonType.

        Args:
            first_name: (str) it is first name of the person.
            last_name: (str) it is last name of the person.
        """

        self.__first_name = first_name
        self.__last_name = last_name

    def __str__(self) -> str:
        return f'First Name: {self.__first_name}\nLast Name: {self.__last_name}'

    @property
    def first_name(self) -> str:
        """
        It returns first name.

        Returns:
            (str): __first_name
        """
        return self.__first_name

    @first_name.setter
    def first_name(self, value: str):
        """
        Set __first_name from the rvalue.
        It must be str and consist of only alphabet.

        Args:
            value: (str) it is rvalue. It can be other types, but it is not allowed.
        """

        # when the value is not str.
        if not isinstance(value, str):
            raise TypeError('It must be str.')

        # when the value does not consist of only alphabet.
        elif not value.isalpha():
            raise ValueError('It must consist of alphabet.')

        self.__first_name = value

    @property
    def last_name(self) -> str:
        """
        It returns last name.

        Returns:
            (str): __last_name
        """
        return self.__last_name

    @last_name.setter
    def last_name(self, value: str):
        """
        Set __last_name from the rvalue.
        It must be str and consist of only alphabet.

        Args:
            value: (str) it is rvalue. It can be other types, but it is not allowed.
        """

        # when the value is not str.
        if not isinstance(value, str):
            raise TypeError('It must be str.')

        # when the value does not consist of only alphabet.
        elif not value.isalpha():
            raise ValueError('It must consist of alphabet.')

        self.__last_name = value


class DoctorType(PersonType):
    """
    This store the doctor's name and speciality.
    It has super class' attributes and speciality.
    All attribute is required.
    """

    def __init__(self, speciality: str, first_name: str, last_name: str):
        """
        Initializer for DoctorType.

        Args:
            speciality: (str) it is the doctor's speciality.
            first_name: (str) it is the doctor's first name.
            last_name:  (str) it is the doctor's last name.
        """

        # call super class' initializer.
        super().__init__(first_name, last_name)
        self.__speciality = speciality

    def __str__(self) -> str:
        return f'\t- Doctor -\n{super().__str__()}\nSpeciality: {self.__speciality}'

    @property
    def speciality(self) -> str:
        """
        It returns speciality

        Returns:
            (str): __speciality
        """
        return self.__speciality

    @speciality.setter
    def speciality(self, value: str):
        """
        Set speciality from the rvalue.

        Args:
            value: (str) it is rvalue. It can be other types, but it is not allowed.
        """

        # when the value is not str.
        if not isinstance(value, str):
            raise TypeError('It must be str.')

        # when the value does not consist of only alphabet.
        elif not value.isalpha():
            raise ValueError('It must consist of alphabet.')

        self.__speciality = value


class DateType:
    def __init__(self, year: int, month: int, day: int):
        self.__year = year
        self.__month = month
        self.__day = day

    def __eq__(self, other) -> bool:
        if not isinstance(other, DateType):
            raise TypeError("It cannot work with different type")

        return (self.year == other.year) and (self.month == other.month) and (self.day == other.day)

    def __sub__(self, other) -> timedelta:
        if not isinstance(other, DateType):
            raise TypeError("It cannot work with different type")

        from datetime import date
        return date(self.year, self.month, self.day) - date(other.year, other.month, other.day)

    def __add__(self, other) -> timedelta:
        if not isinstance(other, DateType):
            raise TypeError("It cannot work with different type")

        from datetime import date
        return date(self.year, self.month, self.day) + date(other.year, other.month, other.day)

    @property
    def year(self) -> int:
        return self.__year

    @property
    def month(self) -> int:
        return self.__month

    @property
    def day(self) -> int:
        return self.__day

    def strftime(self, fstring: str) -> str:
        from datetime import date

        return date(self.year, self.month, self.day).strftime(fstring)

    @classmethod
    def today(cls):
        from datetime import date

        the_date = date.today()
        return DateType(the_date.year, the_date.month, the_date.day)


class PatientType(PersonType):
    """
    This is PatientType for patients.
    It has a lot of attributes, and one class attribute for id.
    The __id is Auto Increased Field when instance is initialized.
    """

    _id = 0

    def __init__(
            self,
            first_name: str,
            last_name: str,
            age: int,
            birthday: DateType,
            attending_physician: DoctorType,
            admitted_date: DateType,
            discharged_date: DateType = None
    ):
        """
        Initialize this class.

        Args:
            first_name: (str) first name of patient
            last_name: (str) last name of patient
            age: (int) age of patient
            birthday: (DateType) patient's date of birth
            attending_physician: (DoctorType) the attending physician for patient
            admitted_date: (DateType) admitted date of patient
            discharged_date: (DateType|None) discharged date of patient
        """

        # call super class' initializer.
        super().__init__(first_name, last_name)

        # increase __id automatically.
        self._id += 1

        # this __id is instance's attribute.
        self.__id = self._id
        self.__age = age
        self.__birthday = birthday
        self.__attending_physician = attending_physician
        self.__admitted_date = admitted_date
        self.__discharged_date = discharged_date

    def __str__(self) -> str:
        return f'''\t- Patient -
ID: {self.__id}
{super().__str__()}
Age: {self.__age}
Birthday: {self.__birthday.strftime("%d/%m/%Y")}
Admitted date: {self.__admitted_date.strftime("%d/%m/%Y")}
Discharged date: {self.__discharged_date.strftime("%d/%m/%Y") if self.__discharged_date is not None else ''}
Duration: {self.duration.days} days

Attending physician: 
{str(self.__attending_physician)}
'''

    @property
    def id(self) -> int:
        """
        It returns patient id.

        Returns:
            (int): __id
        """
        return self.__id

    @property
    def age(self) -> int:
        """
        It returns age.

        Returns:
            (int): __age
        """
        return self.__age

    @property
    def birthday(self) -> DateType:
        """
        It returns birthday of patient.

        Returns:
            (DateType): __birthday
        """
        return self.__birthday

    @property
    def attending_physician(self) -> DoctorType:
        """
        It returns attending physician.

        Returns:
            (DoctorType): __attending_physician
        """
        return self.__attending_physician

    @attending_physician.setter
    def attending_physician(self, value: DoctorType):
        """
        Set __attending_physician from rvalue.
        It must be DoctorType.

        Args:
            value: (DoctorType) it is rvalue. It can be other types, but it is not allowed.
        """

        # when the value is not DoctorType.
        if not isinstance(value, DoctorType):
            raise TypeError('The value has to be only Doctor.')

        self.__attending_physician = value

    @property
    def admitted_date(self) -> DateType:
        """
        It returns admitted date.

        Returns:
            (DateType): __admitted_date
        """
        return self.__admitted_date

    @property
    def discharged_date(self) -> Optional[DateType]:
        """
        It returns discharged date.
        It is intentionally allowed None to distinguish whether it's actually none or today's date.

        Returns:
            (DateType|None): __discharged_date
        """
        return self.__discharged_date

    @discharged_date.setter
    def discharged_date(self, value: DateType):
        """
        Set __discharged_date from rvalue.
        It must be DateType.

        Args:
            value: (DateType) it is rvalue. It can be other types, but it is not allowed.
        """

        # when the value is not date.
        if not isinstance(value, DateType):
            raise TypeError('It must be DateType.')

        # if the value is same date or past date
        elif (value - self.__admitted_date).days <= 0:
            raise ValueError('It must be future DateType.')

        self.__discharged_date = value

    @age.setter
    def age(self, value: int):
        """
        Set __age from the rvalue.
        It must be int.

        Args:
            value: (int) it is rvalue. It can be other types, but it is not allowed.
        """

        # when the value is not int.
        if not isinstance(value, int):
            raise TypeError('It must be int.')

        self.__age = value

    @property
    def duration(self) -> timedelta:
        """
        Calculate duration between admitted date and discharged date.
        If the patient is still hospitalized (if __discharged_date is None), use today's date.

        Returns:
            (timedelta): delta time between dates.
        """

        return (
            self.__discharged_date - self.__admitted_date
            if self.__discharged_date is not None else DateType.today() - self.__admitted_date
        )

    def update_discharged_date_as_today(self):
        """
        Change __discharged_date to today's date.

        There are no any Args and any Returns.
        """
        self.__discharged_date = DateType.today()


class ChargeHistoryItem:
    """
    This class store charge history's columns.

    It is implemented as a class
    because it was more efficient and more readable to use a new class
    than implementing a *dict* with a validation function added.
    """

    # It is available categories.
    # For dynamic adding items or removing items, it is implemented as a list, not Enum.
    categories = ['medicine', 'doctor', 'room']

    def __init__(self, cost: int, category: str, description: str = None):
        """
        Initialize this class

        Args:
            cost: (int) cost for something.
            category: (str) type of cost.
            description: (str|None) additional field.
        """

        # validate category, is it available category or not.
        if not self.validation_category(category):
            raise ValueError(
                'It must be in categories;' + ', '.join(self.categories)
            )

        self.__cost = cost
        self.__category = category
        self.__description = description

    def __str__(self) -> str:
        return f'{self.__category} | {self.__cost} | {self.__description}'

    # this is add-operator overriding functions.
    def __add__(self, other):
        if isinstance(other, ChargeHistoryItem):
            return self.__cost + other.__cost
        else:
            return self.__cost + other

    def __radd__(self, other):
        if isinstance(other, ChargeHistoryItem):
            return self.__cost + other.__cost
        else:
            return self.__cost + other

    @property
    def cost(self) -> int:
        """
        It returns cost.

        Returns:
            (int): __cost
        """
        return self.__cost

    @property
    def category(self) -> str:
        """
        It returns category.

        Returns:
            (str): __category
        """
        return self.__category

    @property
    def description(self) -> Optional[str]:
        """
        It returns description.

        Returns:
            (str|None): __description
        """
        return self.__description

    @description.setter
    def description(self, value: str):
        """
        Set __description from the value.

        Args:
            value: (str) it is rvalue.
        """

        self.__description = value

    @category.setter
    def category(self, value: str):
        """
        Set __category from rvalue.
        It must be str and available.

        Args:
            value: (str) it is rvalue. It can be other types, but it is not allowed.
        """

        # when the value is not str.
        if not isinstance(value, str):
            raise TypeError('It must be str.')

        # when the value is not in available categories.
        if not self.validation_category(value):
            raise ValueError(
                'It must be in categories;' + ', '.join(self.categories)
            )

        self.__category = value

    @classmethod
    def add_new_category(cls, category: str):
        """
        Add new category item in categories.
        It must be str and consist of only alphabet.

        Args:
            category: (str) new category item.
        """

        # when the value is not str.
        if not isinstance(category, str):
            raise TypeError('It must be str.')

        # when the value does not consist of only alphabet.
        elif not category.isalpha():
            raise ValueError('It must consist of alphabet.')

        cls.categories.append(category.lower())

    def validation_category(self, category: str) -> bool:
        """

        Args:
            category:

        Returns:

        """
        return category.lower() in self.categories


class BillType:
    """
    This is Bill type.
    It has patient information and charge history.
    """

    def __init__(self, patient: PatientType):
        """
        Initialize this class.
        patient is required.

        Args:
            patient: (PatientType) patient for bill.
        """

        self.__patient = patient
        self.__charge_history = []

    def __len__(self) -> int:
        return len(self.__charge_history)

    def __getitem__(self, item) -> Union[ChargeHistoryItem, List[ChargeHistoryItem]]:
        if isinstance(item, int):
            return self.__charge_history[item]
        elif isinstance(item, slice):
            return self.__charge_history[item.start:item.stop:item.step]
        else:
            raise TypeError('It must be [int] or [slice]')

    def __str__(self) -> str:
        return f'''\t- bill -
        
{str(self.__patient)}

\t- Charge History - 
''' + f'\n'.join(
            list(map(lambda x: str(x), self.__charge_history))
        ) + f'\n\nTotal: {str(self.total_fee)}'

    @property
    def patient(self) -> PatientType:
        """
        It returns patient.

        Returns:
            (PatientType): __patient
        """

        return self.__patient

    @property
    def total_fee(self) -> int:
        """
        It calculates total fee and returns the result.

        Returns:
            (int): calculated result.
        """

        return sum(self.__charge_history)

    def show_bill(self):
        """
        Show itself using *print()*
        """
        print(self.__str__())

    def add_charge(self, cost: int, category: str, description: str = None):
        """
        Add a new charge in __charge_history.

        Args:
            cost: (int) cost for something.
            category: (str) type of cost.
            description: (str|None) additional field.
        """

        self.__charge_history.append(ChargeHistoryItem(cost, category, description))

    def remove_charge(self, index: int):
        """
        Remove a charge from __charge_history.

        Args:
            index: (int) the charge's index.
        """

        return self.__charge_history.pop(index)
