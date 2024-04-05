from classes.gclass import Gclass
import datetime
class User(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 1   
    nkey= 1
    
    accountbalance = 0.0
    floor = None 
    section = None
    
    att = ['_idcode','_firstname','_lastname','_emailaddress','_dob','_occupation']

    header = 'User'

    des = ['Code','First Name','Last Name','Email address','Date of Birth','Occupation']

    def __init__(self, code, firstname, lastname, emailaddress, dob, occupation):
        super().__init__()

        if code == 'None':
            codes = User.getatlist('_code')
            if codes == []:
                code = str(1)
            else:
                code = str(max(map(int,User.getatlist('_code'))) + 1)

        self._code = str(code)
        self._firstname = firstname
        self._lastname = lastname
        self._emailaddress = emailaddress
        self._dob = datetime.date.fromisoformat(dob)
        self.verifyoccupation(occupation)

        User.obj[code] = self

        User.lst.append(code)
        
    def verifyoccupation(self,occupation):
        if occupation.lower() not in ['estudante','trabalhador']:
            return 'Ocupação Inválida. A ocupação deve ser "estudante" ou "trabalhador".'
        self._occupation = occupation

    @property
    def firstname(self):
        return self._firstname
    
    @property
    def lastname(self):
        return self._lastname

    @property 
    def emailaddress(self):
        return self._emailaddress
    
    @emailaddress.setter 
    def emailaddress(self,emailaddress):
        self._emailaddress = emailaddress
    
    @property
    def dob(self):
        return self._dob

    @property
    def occupation(self):
        return self._occupation

    @occupation.setter
    def occupation(self, occupation):
        self._occupation = occupation

    def age(self):
        tday = datetime.date.today()
        age = tday.year - self.dob.year
        if tday.month < self.dob.month or \
            (tday.month == self.dob.month and tday.day < self.dob.day):
            age -= 1
        return age
    