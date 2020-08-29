#this is a really simple project for finding the service provider 
#prerequisites: python installed, phonenumbers module installed(pip install phonenumbers)

mobileNo = input("please enter your mobile number")

service_provider = phonenumbers.parse(mobileNo)

print(carrier.name_for_number(service_provider, "en"))

#thanks for sticking through.. this was just a simple python project for finding the service provider of your mobile number
