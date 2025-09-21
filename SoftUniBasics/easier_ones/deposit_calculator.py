deposited_sum = float(input("What sum would you like to deposit: "))
term_of_deposit = float(input("Enter the time of deposit (1 to 12 months): "))
yearly_rate = float(input("Enter yearly rate: "))

amount_to_receive = deposited_sum + term_of_deposit * ((deposited_sum * yearly_rate / 100) / 12)

print(amount_to_receive)