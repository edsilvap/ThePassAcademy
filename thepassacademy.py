#!/usr/bin/env python3

from essential import myfunctions, wordlists


def logo():
    print('''

   \033[1;34m╔════╦╗─────╔═══╗─────────╔═══╗───────╔╗    by
   ║╔╗╔╗║║─────║╔═╗║─────────║╔═╗║───────║║ @edslvp
   ╚╝║║╚╣╚═╦══╗║╚═╝╠══╦══╦══╗║║─║╠══╦══╦═╝╠══╦╗╔╦╗─╔╗
   ──║║─║╔╗║║═╣║╔══╣╔╗║══╣══╣║╚═╝║╔═╣╔╗║╔╗║║═╣╚╝║║─║║\033[1;m
   \033[1;35m──║║─║║║║║═╣║║──║╔╗╠══╠══║║╔═╗║╚═╣╔╗║╚╝║║═╣║║║╚═╝║
   ──╚╝─╚╝╚╩══╝╚╝──╚╝╚╩══╩══╝╚╝─╚╩══╩╝╚╩══╩══╩╩╩╩═╗╔╝
   ─────────────────────────────────────────────╔═╝║
   ─────────────────────────────────────────────╚══╝\033[1;m
     T H E  P A S S W O R D  G E N E R A T O R
     ''')


def main():
    try:
        while True:
            logo()
            print('''

\033[1;35m1)\033[1;m Password Generator

\033[1;35m2)\033[1;m Password Decifer



\033[1;33m[help] to help\033[1;m
            ''')

            opc = input('\033[1;34mtpa > \033[1;m')
            while opc == '1':
                print('''


\033[1;35m1)\033[1;m Password Generator [five dice]

\033[1;35m2)\033[1;m Password Generator [four dice]



\033[1;33m[back] to home\033[1;m
                ''')

                opc1 = input('\033[1;34mtpa > \033[1;m')
                if opc1 == '1':
                    r = myfunctions.roll_dice5()
                    a = myfunctions.roll_dice5()
                    n = myfunctions.roll_dice5()
                    d = myfunctions.roll_dice5()
                    o = myfunctions.roll_dice5()
                    m = myfunctions.roll_dice5()

                    pass_id = r + a + n + d + o + m

                    pass_gen = myfunctions.password_generator(r, a, n, d, o, m, **wordlists.wordlist_5d)
                    logo()
                    print(f'''
   \033[1;32mP A S S
   W O R D [ {pass_gen} ]\033[1;m
   -------
   \033[1;34mP A S S
     I D   [ {pass_id} ]\033[1;m
                    ''')
                elif opc1 == '2':
                    r = myfunctions.roll_dice4()
                    a = myfunctions.roll_dice4()
                    n = myfunctions.roll_dice4()
                    d = myfunctions.roll_dice4()
                    o = myfunctions.roll_dice4()
                    m = myfunctions.roll_dice4()

                    pass_id = r + a + n + d + o + m

                    pass_gen = myfunctions.password_generator(r, a, n, d, o, m, **wordlists.wordlist_4d)
                    logo()
                    print(f'''
   \033[1;32mP A S S
   W O R D [ {pass_gen} ]\033[1;m
   -------
   \033[1;34mP A S S
     I D   [ {pass_id} ]\033[1;m
                    ''')
                elif opc1 == 'back':
                    main()
                else:
                    print('\n\033[1;31m[WARNING] Comando invalido\033[1;m')
            while opc == '2':
                print('''


\033[1;35mInput Password ID to Decrypt\033[1;m



\033[1;33m[back] to home\033[1;m
                ''')

                opc2 = input('\033[1;34mtpa > \033[1;m')
                opc2_tam = len(opc2)
                if opc2_tam == 24:
                    try:
                        a = opc2[0:4]
                        b = opc2[4:8]
                        c = opc2[8:12]
                        d = opc2[12:16]
                        e = opc2[16:20]
                        f = opc2[20:24]

                        pass_dec = myfunctions.password_decifer(a, b, c, d, e, f, **wordlists.wordlist_4d)

                        logo()
                        print(f'''
   \033[1;32mP A S S
   W O R D [ {pass_dec} ]\033[1;m
   -------
   \033[1;34mP A S S
     I D   [ {opc2} ]\033[1;m
                         ''')

                    except KeyError:
                        print('\n\033[1;31m[WARNING] Key invalido\033[1;m')

                elif opc2_tam == 30:
                    try:
                        a = opc2[0:5]
                        b = opc2[5:10]
                        c = opc2[10:15]
                        d = opc2[15:20]
                        e = opc2[20:25]
                        f = opc2[25:30]

                        pass_dec = myfunctions.password_decifer(a, b, c, d, e, f, **wordlists.wordlist_5d)

                        logo()
                        print(f'''
   \033[1;32mP A S S
   W O R D [ {pass_dec} ]\033[1;m
   -------
   \033[1;34mP A S S
     I D   [ {opc2} ]\033[1;m
                         ''')

                    except KeyError:
                        print('\n\033[1;31m[WARNING] Key invalido\033[1;m')

                elif opc2 == 'back':
                    main()
                else:
                    print('\n\033[1;31m[WARNING] Tamanho da key invalido\033[1;m')
            while opc == 'help':
                print('''

GitHub: @edsilvap
Instagram: @edslvp


\033[1;33m[back] to home\033[1;m
                ''')

                opc3 = input('\033[1;34mtpa > \033[1;m')
                if opc3 == 'back':
                    main()
                else:
                    print(f'\n\033[1;31m[WARNING] Comando invalido\033[1;m')
    except KeyboardInterrupt:
        print('bye bye')
main()
