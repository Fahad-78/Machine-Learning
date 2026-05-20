#Extract username from a given email.
#Eg if the email is nitish24singh@gmail.com
#then the username should be nitish24singh

s = input('Enter email name: ')

position = s.index('@')

print(s[0:position])