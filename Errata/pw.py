#! python3
# pw.py - An insecure password locker program

PASSWORDS = {'email': 'ksjf9924j65nGR',
             'blog': 'SDGFwh23',
             'luggage': '12345'}
import sys, pyperclip
if len(sys.argv) < 2:
   print("I'm sorry, but which program were you looking to login to?")
   print('Usage: python py.py [account] - copy account password')
   sys.exit()
   
sccount = sys.argv[1] #The First command line argument is the account name

if account in PASSWORDS:
   pyperclip.copy(PASSWORDS[account])
   print('Password for' + account + 'copied to clipboard.')
else:
   print('There is no account found named ' + account)
