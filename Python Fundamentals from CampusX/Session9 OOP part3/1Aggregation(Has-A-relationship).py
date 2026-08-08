'''
There are tow types of class relationship
    ->Aggregation
    ->Inheritence
    
Inheritence is mostly used, but we will also learn aggregation
'''
#Aggregation example
class Customer:
    def __init__(self,name, gender, address):
        self.name = name
        self.gender = gender
        self.address = address

    def print_info(self):
        print(self.name)
        print(self.gender)
        print(self.address.get_city())
        print(cust.address.pin)
        print(cust.address.country,'\n')

    def edit_profile(self, new_name, new_city, new_pin, new_country):
        self.name = new_name
        self.address.edit_address(new_city,new_pin,new_country)

class Address:
    def __init__(self,city,pin,country):
        self.__city = city
        self.pin = pin
        self.country = country

    def get_city(self):
        return self.__city
        '''
        A important things is that if we private any variable
        like self.city -> self.__city then def print_address can't access the city.
        For accessing the varible we have to make a method under Address class name get_city, where it will return self.__city
        '''

    def edit_address(self, new_city, new_pin, new_country):
        self.__city = new_city
        self.pin = new_pin
        self.country = new_country

add1 = Address('Dhaka',1230,'Bangladesh')
cust = Customer('Fahad','male',add1)
cust.print_info()

cust.edit_profile('Rahat','Gazipur',1222,'Ireland')
cust.print_info()
#method
#

