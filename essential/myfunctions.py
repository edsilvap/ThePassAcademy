from random import randint

def inputme():
	input_me = input('\033[1;34mtpa > \033[1;m')
	return input_me


def randice():
	dice = randint(1, 6)
	return dice


def roll_5_dice():
	roll_1 = str(randice())
	roll_2 = str(randice())
	roll_3 = str(randice())
	roll_4 = str(randice())
	roll_5 = str(randice())
	roll_out = roll_1 + roll_2 + roll_3 + roll_4 + roll_5
	return roll_out


def roll_4_dice():
	roll_1 = str(randice())
	roll_2 = str(randice())
	roll_3 = str(randice())
	roll_4 = str(randice())
	roll_out = roll_1 + roll_2 + roll_3 + roll_4
	return roll_out


def password_generator(param_1, param_2, param_3, param_4, param_5, param_6, **wordlist):
	password_gen_1 = wordlist[param_1]
	password_gen_2 = wordlist[param_2]
	password_gen_3 = wordlist[param_3]
	password_gen_4 = wordlist[param_4]
	password_gen_5 = wordlist[param_5]
	password_gen_6 = wordlist[param_6]
	password_gen_out = password_gen_1 + password_gen_2 + password_gen_3 + password_gen_4 + password_gen_5 + password_gen_6
	return password_gen_out


def password_decrypt(param_1, param_2, param_3, param_4, param_5, param_6, **wordlist):
	password_decrypt_1 = wordlist[param_1]
	password_decrypt_2 = wordlist[param_2]
	password_decrypt_3 = wordlist[param_3]
	password_decrypt_4 = wordlist[param_4]
	password_decrypt_5 = wordlist[param_5]
	password_decrypt_6 = wordlist[param_6]
	password_decrypt_out = password_decrypt_1 + password_decrypt_2 + password_decrypt_3 + password_decrypt_4 + password_decrypt_5 + password_decrypt_6
	return password_decrypt_out


def printme(valor_1, valor_2):
	print(f'''
   \033[1;32mP A S S
   W O R D [ {valor_1} ]\033[1;m
   -------
   \033[1;34mP A S S
     I D   [ {valor_2} ]\033[1;m
	''')
