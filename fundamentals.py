# BREAK STATEMENT
names = ['John', 'Shalom', 'Abigail', '', 'Naomi']
for name in names:
    if name == '':
        print('empty value detected')
        break
    print(f'NAME: {name}')

    # CONTINUE STATEMENT
countries = ['USA', 'England', 'India', '', 'Turkey']
for country in countries:
    if country == '':
        print('empty value detected')
        continue
    print(f'COUNTRY: {country}')

    # PASS STATEMENT
    days = ['WED', 'THUR', '', 'SUN', 'FRI']
for day in days:
    if day == '':
        pass
    print(f'DAY: {day}')
