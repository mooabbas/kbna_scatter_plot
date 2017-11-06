bold = "\033[1m"
reset = "\033[0;0m"
dollar = float(input('What ' + bold + 'is' + reset + ' the amount of US Dollars you wish to convert ? '))
exchange_rate = float(input('What ' + bold + 'is' + reset + ' the current exchange rate'
                            '\n(1 US Dollar equals what in the Foreign Currency)? '))
amount = float(dollar * exchange_rate)
print('The amount ' + bold + 'in' + reset + ' the Foreign Currency is $%.2f' % amount)
