num = int(input("insert days!:"))
year = num//365
num = num % 365
if year >= 4:
    num = num-(year//4)
    if num <= 186:
        month = num//31
        num = num % 31
        day = num
        print(year, 'sal/', month, 'mah/', day, 'roz')
    elif num >= 186:
        num = num-186
        month = (num//30) + 6
        num = num % 30
        day = num
        print(year, 'sal/', month, 'mah/', day, 'roz')
    else:
        print('your number is incorrect!')
elif year<=4:
    if num <= 186:
        month = num//31
        num = num % 31
        day = num
        print(year, 'sal/', month, 'mah/', day, 'roz')
    elif num >= 186:
        num = num-186
        month = (num//30) + 6
        num = num % 30
        day = num
        print(year, '/', month, '/', day)
    else:
        print('your number is incorrect!')
else:
    print('your number is incorrect!')