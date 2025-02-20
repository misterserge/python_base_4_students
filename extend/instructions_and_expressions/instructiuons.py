name = 'Username' # assing a var
if name:      # if var is not empty
    print(name)

import datetime # import module

today = datetime.date.today() # get today date here



def return_instructions(date):
    if date == datetime.date.today():
        return 'Today is {}'.format(date)
    else:
        return 'Today is not {}'.format(date)

print(return_instructions(today))