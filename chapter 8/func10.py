#  python function that converts inches to cms.
def convert(a):
	cm1 = float(a*2.54)
	return cm1    
print("\nEnter value in Inch : ")
inch = int(input());
cm=convert(inch)
print(inch ," inch is equal to ", cm ," centimeter ")   #here this code helps us to solve the problem