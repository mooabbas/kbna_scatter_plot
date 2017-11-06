cm = float(input('How many centimeters do you want to convert ? '))
yards = int(cm / 91.44)
feet = int(cm / 30.48)
inches = float(cm / 2.54)
print('This is %d yards , %d feet , %f inches .' % (yards, feet, inches))

