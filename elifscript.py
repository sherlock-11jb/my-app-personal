# we are using elif statement to use multiple conditions con OTW 

print ("what is your name?")
name=input()

print("what is your age?")
age=input()

if name == "OTW":
    print("hi OTW")
    
elif int(age) < 40:
	print ("you are too young to be OTW")
	
elif int(age) > 100:
	print("you are in danger era of COVID")
	
elif int(age) > 150: 
	print("you must be a zombie")
