a = float(input('enter the amount'))
c = float(input('enter the cash'))
r = float(c - a)
u = [20, 10, 5, 1, 0.25, 0.1, 0.05, 0.01]

twenty = int(r / u[0])
reminder_twenty = r - (int(r / u[0]) * u[0])

ten = int(reminder_twenty / u[1])
reminder_ten = reminder_twenty - (ten * u[1])

five = int(reminder_ten / u[2])
reminder_five = reminder_ten - (five * u[2])

one = int(reminder_five / u[3])
reminder_one = reminder_five - (one * u[3])

quarter = int(reminder_one / u[4])
reminder_quarter = reminder_one - (quarter * u[4])

dime = int(reminder_quarter / u[5])
reminder_dime = reminder_quarter - (dime * u[5])

nickle = int(reminder_dime / u[6])
reminder_nickle = reminder_dime - (nickle * u[6])

penny = int(reminder_nickle / u[7])
reminder_penny = int(reminder_nickle - (penny * u[7]))
print('%d twenties'
      '\n%d tens'
      '\n%d fives'
      '\n%d ones'
      '\n%d quarters'
      '\n%d dimes'
      '\n%d nickles'
      '\n%d pennies' % (twenty, ten, five, one, quarter, dime, nickle, penny))
