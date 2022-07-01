"""house_type: str = "Slytherin"
cause_type: str = "me apetece"
quantity: int = 100
roi_time: int = 3
roi_interest: int = 0.5"""

house_type = input("Enter your house: ")
cause_type = input("Enter the cause: ")
quantity= input("Enter the quantity in golden coins: ")
roi_time= input("Enter in how much time you would like to return the money (in years): ")
roi_interest = input("Enter the interest in %: ")
#float(roi_interest= input("Enter the interest in %: "))
#roi_real_total = int(quantity)*((float(1+roi_interest))**int(roi_time))
roi_total = float(quantity) + float(quantity) * float(roi_time) * float(roi_interest) / 100
#roi_total = input("What is the total amount of money you will give back the Governor of the Iron Bank? ")
#bool(want_to_define_roi_total= input("Do you want to overwrite the default quantity needed to return? ",roi_real_total))
#if want_to_define_roi_total=

#roi_total = quantity*(1*roi_interest)**roi_time

#print(roi_total)


print("Dear Governor of the Iron Bank,\n"
"Given the current situation that King’s Landing is facing, the House " + str(house_type) +
" is asking for your economic services because of the following cause: " + cause_type +".\n"
"The estimated total quantity is " +str(quantity) + " gold coins. The loan will be returned during the "+ str(roi_time)+
" following years with "+ str(roi_interest) +" % of bank interest. \nThus, the money recovered from the bank,"
" once the loan is completely returned, will be " +str(roi_total)+ " gold coins.\n"
"I hope the bank will consider this proposal because the House " + str(house_type) +" always pays its debts.\n"
"Signed: \n \nLord Mace Tyrell \n \t\tLannister’s Master of Coin\n"
"\t \t“Lord of Highgarden and Warden of the South”\n" )