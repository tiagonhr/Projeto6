# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 10:32:08 2024

@author: up202304973
"""

from classes.gclass import Gclass
import datetime
class Room(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0 
    nkey= 1
    
    Section = ['A','B']
    Floor = [1,2,3,4,5,6,7,8]
    Rooms = {'Normais':10,'Estúdios':5,'Duplos':5}
    Price = {'Normais':500,'Estúdios':550,'Duplos':300}
    occupation = [[0]*20]*8
    
    att = ['_section','_floor','_tipology','_room']

    header = 'Room'

    des = ['Section','Floor','Tipology','Room']

    def __init__(self, section, floor, tipology, room):
        super().__init__()

        # if code == 'None':
        #     codes = Room.getatlist('_code')
        #     if codes == []:
        #         code = str(1)
        #     else:
        #         code = str(max(map(int,Room.getatlist('_code'))) + 1)

        self._section = section
        self._floor = floor
        self._tipology = tipology
        self._room = room
        code = self._section + self._floor + self._tipology[0] + self._room

        Room.obj[code] = self

        Room.lst.append(code)

    @property
    def section(self):
        return self._section
    
    @property
    def floor(self):
        return self._floor

    @property 
    def tipology(self):
        return self._tipology
    
    @property
    def room(self):
        return self._room