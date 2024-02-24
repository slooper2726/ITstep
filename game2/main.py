print('Вгадай тварину.')
print('Ця тварина має панцир, і деякі види цієї тварини можуть жити да 130 років.')
print('Живе на суші, і у воді.')
answer = input('Хто це? ')
answer = answer.lower()
if answer == 'черепаха' or answer == 'черепашка':
    print('Правильно!')
    print('  ___')
    print(' //_\\\\ _')
    print("/_|_|_('>")
    print(' "   "')
else:
    print('Не правильно!')
