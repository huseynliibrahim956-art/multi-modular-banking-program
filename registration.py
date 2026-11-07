#registrationn_part
import numpy as np
class user:
    def __init__(self,name,phone_num,country,card_type,via_code):
        self.name=name
        self.phone_num=phone_num
        self.country=country
        self.card_type=card_type
        self.via_code=via_code
    def namess():
        names=input('enter your name')
        return names
    def phone_nums():
        try:
         phone_num=int(input('phone num:'))
         return phone_num
        except ValueError:
           print('you should have entered phone num coonsists of integers not floats or strings')
           pass
    def countrys():
       countrys=input('country:').lower()
       return countrys
    def card_types():
       card=input('what sort of card do you wanna have debit or credit?').lower()
       if card=='debit':
          return card
       elif card=='credit':
          return card
       else:
          pass
nam=user.namess()
num=user.phone_nums()
count=user.countrys()
cardt=user.card_types()
rng=np.random.default_rng()
array1=np.array([234678,768967,324789,980706,176839,997863])
via_Codes=rng.choice(array1)
user1=user(name=nam,phone_num=num,country=count,card_type=cardt,via_code=via_Codes)