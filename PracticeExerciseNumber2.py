enter=float(input('How far would you like to travel in miles?'))
if enter<=3:
    print('I suggest walking to your destination.')
elif 3<=enter<300:
    print('I suggest driving to your destination.')
else :
    print('I suggest flying to your destination.')

