print('This program is to check if the patients are healthy or unhealthy.')
print('------------------------------------------------------------------')

class Patient:
    def __init__(self, name, sugar, fat, salt):
        self.name = name
        self.sugar = float(sugar)
        self.fat = float(fat)
        self.salt = float(salt)

    def healthy(self):
        if self.sugar <= 37.5 and self.fat <= 77 and self.salt <= 2300:
            print(f'The patient {self.name} is healthy')
        else:
            print(f'The patient {self.name} is unhealthy')

while True:
    try:
        i = int(input('How many patients do you want to enter? '))
        break
    except ValueError:
        print('Please enter a valid number.')

while True:
    try:
        for j in range(i):
            print('Patient number ', j + 1)
            patient = Patient(str(input('Enter your name: ')),
                              float(input('Enter your sugar intake(g): ')),
                              float(input('Enter your fat intake(g): ')),
                              float(input('Enter your salt intake(mg): ')))
            print(patient.healthy())
            j += 1
        break
    except ValueError:
        print('Please enter valid information.')

print('Please worry that for a healthy person the sugar intake must be below 37.5g, '
      'the fat intake below 77g, and the salt intake per day below 2300mg!')

input('\nPress enter to finish the program.')
