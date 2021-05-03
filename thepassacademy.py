#!/usr/bin/env python3
import sys
from os import system
from essential import myfunctions, wordlists

so = sys.platform

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

\033[1;35m[ 1 ]\033[1;m Password Generator

\033[1;35m[ 2 ]\033[1;m Password Decrypt



\033[1;33m[help] to help\033[1;m
            ''')

            input_main = myfunctions.inputme()
            while input_main == '1':
                print('''


\033[1;35m[ 1 ]\033[1;m Password Generator [five dice]

\033[1;35m[ 2 ]\033[1;m Password Generator [four dice]



\033[1;33m[back] to home | [clear] to clear\033[1;m
                ''')

                input_1 = myfunctions.inputme()
                if input_1 == '1':
                    r = myfunctions.roll_5_dice()
                    a = myfunctions.roll_5_dice()
                    n = myfunctions.roll_5_dice()
                    d = myfunctions.roll_5_dice()
                    o = myfunctions.roll_5_dice()
                    m = myfunctions.roll_5_dice()

                    password_id = r + a + n + d + o + m

                    password_gen = myfunctions.password_generator(r, a, n, d, o, m, **wordlists.wordlist_5_dice)

                    logo()

                    myfunctions.printme(password_gen, password_id)

                elif input_1 == '2':
                    r = myfunctions.roll_4_dice()
                    a = myfunctions.roll_4_dice()
                    n = myfunctions.roll_4_dice()
                    d = myfunctions.roll_4_dice()
                    o = myfunctions.roll_4_dice()
                    m = myfunctions.roll_4_dice()

                    password_id = r + a + n + d + o + m

                    password_gen = myfunctions.password_generator(r, a, n, d, o, m, **wordlists.wordlist_4_dice)

                    logo()

                    myfunctions.printme(password_gen, password_id)
                elif input_1 == 'clear' and so == 'linux':
                    system('clear')

                elif input_1 == 'clear' and so == 'win32':
                    system('cls')

                elif input_1 == 'back':
                    main()

                else:
                    print('\n\033[1;31m[WARNING] Comando invalido\033[1;m')

            while input_main == '2':
                print('''


\033[1;35m<\033[1;m Input Password ID to Decrypt \033[1;35m>\033[1;m



\033[1;33m[back] to home | [clear] to clear\033[1;m
                ''')

                input_2 = myfunctions.inputme()
                input_2_tam = len(input_2)
                if input_2_tam == 24:
                    try:
                        a = input_2[0:4]
                        b = input_2[4:8]
                        c = input_2[8:12]
                        d = input_2[12:16]
                        e = input_2[16:20]
                        f = input_2[20:24]

                        pass_dec = myfunctions.password_decrypt(a, b, c, d, e, f, **wordlists.wordlist_4_dice)

                        logo()

                        myfunctions.printme(pass_dec, input_2)

                    except KeyError:
                        print('\n\033[1;31m[WARNING] Key invalido\033[1;m')

                elif input_2_tam == 30:
                    try:
                        a = input_2[0:5]
                        b = input_2[5:10]
                        c = input_2[10:15]
                        d = input_2[15:20]
                        e = input_2[20:25]
                        f = input_2[25:30]

                        pass_dec = myfunctions.password_decrypt(a, b, c, d, e, f, **wordlists.wordlist_5_dice)

                        logo()

                        myfunctions.printme(pass_dec, input_2)

                    except KeyError:
                        print('\n\033[1;31m[WARNING] Key invalido\033[1;m')

                elif input_2 == 'clear' and so == 'linux':
                    system('clear')

                elif input_2 == 'clear' and so == 'win32':
                    system('cls')

                elif input_2 == 'back':
                    main()

                else:
                    print('\n\033[1;31m[WARNING] Tamanho da key invalido\033[1;m')

            while input_main == 'help':
                print('''

GitHub: @edsilvap
Instagram: @edslvp


\033[1;33m[back] to home | [clear] to clear\033[1;m
                ''')

                input_3 = myfunctions.inputme()
                if input_3 == 'clear' and so == 'linux':
                    system('clear')

                elif input_3 == 'clear' and so == 'win32':
                    system('cls')

                elif input_3 == 'back':
                    main()

                else:
                    print(f'\n\033[1;31m[WARNING] Comando invalido\033[1;m')
    except KeyboardInterrupt:
        print('bye bye')
    sys.exit(1)

if __name__ == '__main__':
    main()
