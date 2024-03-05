# -*- coding: utf-8 -*-
"""
@author: António Brito / Carlos Bragança
(2024)
#objective: class Person

"""""
#%% Class Person v2
import datetime
class Person:
    # Dictionary of objects person
    obj = dict()
    lst = list()
    pos = 0
    # Constructor: Called when an object is instantiated
    def __init__(self, code, name, dob, salary):
        # Object attributes
        self._code = code
        self._name = name
        doblist = list(map(int, dob.split('-')))
        self._dob = datetime.date(doblist[0], doblist[1], doblist[2])
        self._salary = float(salary)
        # Add the new object to the Person list
        Person.obj[code] = self
        Person.lst.append(code)

    # code property getter method
    @property
    def code(self):
        return self._code
    @code.setter
    def code(self, code):
        self._code = code
    # name property getter method
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name
    # dob property getter method
    @property
    def dob(self):
        return self._dob
    # dob property setter method
    @dob.setter
    def dob(self, dob):
        self._dob = dob
    # salary property getter method
    @property
    def salary(self):
        return self._salary
    # salary property setter method
    @salary.setter
    def salary(self, salary):
        self._salary = salary

    # Class method to implement constructor overloading
    @classmethod
    def from_string(cls, person_data):
        args_list = person_data.split(";")
        return cls(args_list[0], args_list[1], args_list[2], float(args_list[3]))
    @classmethod
    def nextrec(cls):
        cls.pos += 1
        return cls.current()
    @classmethod
    def previous(cls):
        cls.pos -= 1
        return cls.current()
    @classmethod
    def current(cls):
        if cls.pos < 0:
            cls.pos = 0
            return None
        elif cls.pos >= len(cls.lst):
            cls.pos = len(cls.lst) - 1
            return None
        else:
            code = cls.lst[cls.pos]
            return cls.obj[code]
    @classmethod
    def first(cls):
        cls.pos = 0
        return cls.current()
    @classmethod
    def last(cls):
        cls.pos = len(cls.lst) - 1
        return cls.current()
    # Object delete method
    @classmethod
    def remove(cls, p):
        cls.lst.remove(p)
        del cls.obj[p]
        del p
    # Write object to csv file
    @classmethod
    def write(cls, path = ''):
        fh = open(path + 'Person.csv', 'w')
        fh.write('code;name;dob;salary\n')
        for p in Person.obj.values():
            fh.write(p.__str__() + '\n')
        fh.close()
    # Read objects from csv file
    @classmethod
    def read(cls, path = ''):
        cls.obj = dict()
        cls.lst = list()
        try:
            fh = open(path + 'Person.csv', 'r')
            fh.readline()
            for p in fh:
                cls.from_string(p.strip())
            fh.close()
        except BaseException as err:
            print(f"Error in read method:\n{err}\n{type(err)}")
    # Method to return object info
    def __str__(self):
        return f'{self.code};{self.name};{self.dob};{self.salary}'
