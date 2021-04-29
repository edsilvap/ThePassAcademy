from random import randint


def ran():
	a = randint(1, 6)
	return a


def roll_dice5():
	resultA = str(ran())
	resultB = str(ran())
	resultC = str(ran())
	resultD = str(ran())
	resultE = str(ran())
	out_roll = resultA + resultB + resultC + resultD + resultE
	return out_roll


def roll_dice4():
	resultA = str(ran())
	resultB = str(ran())
	resultC = str(ran())
	resultD = str(ran())
	out_roll = resultA + resultB + resultC + resultD
	return out_roll


def password_generator(parmR, parmA, parmN, parmD, parmO, parmM, **wrdlst):
	pass1 = wrdlst[parmR]
	pass2 = wrdlst[parmA]
	pass3 = wrdlst[parmN]
	pass4 = wrdlst[parmD]
	pass5 = wrdlst[parmO]
	pass6 = wrdlst[parmM]
	out_gen = pass1 + pass2 + pass3 + pass4 + pass5 + pass6
	return out_gen


def password_decifer(prm1, prm2, prm3, prm4, prm5, prm6, **kwarg):
	dec1 = kwarg[prm1]
	dec2 = kwarg[prm2]
	dec3 = kwarg[prm3]
	dec4 = kwarg[prm4]
	dec5 = kwarg[prm5]
	dec6 = kwarg[prm6]
	dec = dec1 + dec2 + dec3 + dec4 + dec5 + dec6
	return dec
