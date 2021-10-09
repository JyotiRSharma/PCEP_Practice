year = int(input("Enter a year: "))

#
# Write your code here.
#	
if year < 1582:
    print('Not within the Gregorian calendar period')
    exit(0)

res = ''
# if the year number isn't divisible by four, it's a common year;
if year%4 != 0:
    res = 'Common year'
# otherwise, if the year number isn't divisible by 100, it's a leap year;
elif year%100 != 0:
    res = 'Leap year'
# otherwise, if the year number isn't divisible by 400, it's a common year;
elif year%400 != 0:
    res = 'Common year'
# otherwise, it's a leap year.
else:
    res = 'Leap year'
    
print(res)
